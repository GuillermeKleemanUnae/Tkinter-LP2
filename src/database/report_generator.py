"""
Generación de Reportes Usando "Data Report"

Los reportes son una parte fundamental de cualquier sistema de información.
Permiten presentar los datos de manera organizada y comprensible para
facilitar la toma de decisiones.

Este módulo proporciona funcionalidades para generar diferentes tipos de reportes:
- Reportes en formato PDF
- Reportes en formato Excel
- Reportes en formato CSV
- Reportes en formato HTML
- Reportes estadísticos

Utiliza librerías como ReportLab para PDF, pandas para Excel/CSV,
y genera reportes estructurados con gráficos y tablas.
"""

from typing import List, Dict, Any, Optional
import sqlite3
from datetime import datetime, date
import os
import json
from pathlib import Path

# Importaciones para generación de reportes
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("⚠️  ReportLab no está instalado. Instalar con: pip install reportlab")

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("⚠️  Pandas no está instalado. Instalar con: pip install pandas")

from .connection import DatabaseConnection
from .dao import StudentDAO, CourseDAO, EnrollmentDAO

class ReportGenerator:
    """
    Generador de reportes para el sistema educativo
    Proporciona múltiples formatos de salida y tipos de reportes
    """
    
    def __init__(self, output_directory: str = "reports"):
        self.db = DatabaseConnection()
        self.student_dao = StudentDAO()
        self.course_dao = CourseDAO()
        self.enrollment_dao = EnrollmentDAO()
        
        # Crear directorio de reportes si no existe
        self.output_dir = Path(output_directory)
        self.output_dir.mkdir(exist_ok=True)
        
        # Configurar estilos para reportes
        self.setup_report_styles()
    
    def setup_report_styles(self):
        """Configura los estilos para los reportes"""
        if REPORTLAB_AVAILABLE:
            self.styles = getSampleStyleSheet()
            # Crear estilos personalizados
            self.styles.add(ParagraphStyle(
                name='CustomTitle',
                parent=self.styles['Heading1'],
                fontSize=16,
                spaceAfter=30,
                alignment=1,  # Centro
                textColor=colors.darkblue
            ))
            self.styles.add(ParagraphStyle(
                name='CustomHeading',
                parent=self.styles['Heading2'],
                fontSize=12,
                spaceAfter=12,
                textColor=colors.darkblue
            ))
    
    # ========================================
    # REPORTES DE ESTUDIANTES
    # ========================================
    
    def generate_student_report(self, format_type: str = "pdf", 
                               filter_status: str = None) -> str:
        """
        Genera un reporte completo de estudiantes
        
        Args:
            format_type: "pdf", "excel", "csv", "html"
            filter_status: "active", "inactive", "graduated" o None para todos
        """
        try:
            # Obtener datos de estudiantes
            if filter_status:
                students = self.student_dao.get_by_status(filter_status)
            else:
                students = self.student_dao.get_all()
            
            report_data = []
            for student in students:
                # Obtener inscripciones del estudiante
                enrollments = self.enrollment_dao.get_by_student(student.id)
                total_courses = len(enrollments)
                completed_courses = len([e for e in enrollments if e.status == 'completed'])
                avg_grade = sum([e.grade for e in enrollments if e.grade is not None]) / len([e for e in enrollments if e.grade is not None]) if enrollments else 0
                
                report_data.append({
                    'ID': student.id,
                    'Nombre': student.first_name,
                    'Apellido': student.last_name,
                    'Email': student.email,
                    'Teléfono': student.phone or '',
                    'Estado': student.status,
                    'Fecha Inscripción': student.enrollment_date,
                    'Cursos Inscritos': total_courses,
                    'Cursos Completados': completed_courses,
                    'Promedio': round(avg_grade, 2) if avg_grade > 0 else 'N/A'
                })
            
            # Generar reporte según el formato
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reporte_estudiantes_{timestamp}"
            
            if format_type.lower() == "pdf":
                return self._generate_pdf_report(report_data, filename, "Reporte de Estudiantes")
            elif format_type.lower() == "excel":
                return self._generate_excel_report(report_data, filename, "Estudiantes")
            elif format_type.lower() == "csv":
                return self._generate_csv_report(report_data, filename)
            elif format_type.lower() == "html":
                return self._generate_html_report(report_data, filename, "Reporte de Estudiantes")
            else:
                raise ValueError(f"Formato no soportado: {format_type}")
                
        except Exception as e:
            print(f"✗ Error generando reporte de estudiantes: {e}")
            raise
    
    def generate_student_transcript(self, student_id: int, format_type: str = "pdf") -> str:
        """
        Genera un historial académico individual de un estudiante
        """
        try:
            student = self.student_dao.get_by_id(student_id)
            if not student:
                raise ValueError(f"Estudiante con ID {student_id} no encontrado")
            
            # Obtener historial académico
            query = """
            SELECT 
                c.name as course_name,
                c.code as course_code,
                c.credits,
                e.grade,
                e.status,
                e.enrollment_date,
                c.instructor
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.student_id = ?
            ORDER BY e.enrollment_date
            """
            
            rows = self.db.execute_query(query, (student_id,))
            transcript_data = []
            total_credits = 0
            total_grade_points = 0
            
            for row in rows:
                course_data = {
                    'Código': row['course_code'],
                    'Curso': row['course_name'],
                    'Créditos': row['credits'],
                    'Calificación': row['grade'] if row['grade'] is not None else 'En Progreso',
                    'Estado': row['status'],
                    'Fecha Inscripción': row['enrollment_date'],
                    'Instructor': row['instructor'] or 'N/A'
                }
                transcript_data.append(course_data)
                
                if row['grade'] is not None and row['status'] == 'completed':
                    total_credits += row['credits']
                    total_grade_points += row['grade'] * row['credits']
            
            # Calcular GPA
            gpa = total_grade_points / total_credits if total_credits > 0 else 0
            
            # Información del estudiante
            student_info = {
                'Nombre Completo': student.full_name,
                'Email': student.email,
                'Estado': student.status,
                'Fecha de Inscripción': student.enrollment_date,
                'Créditos Totales': total_credits,
                'GPA': round(gpa, 2)
            }
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"historial_{student.last_name}_{student.first_name}_{timestamp}"
            
            if format_type.lower() == "pdf":
                return self._generate_transcript_pdf(student_info, transcript_data, filename)
            else:
                return self._generate_excel_report(transcript_data, filename, "Historial Académico")
                
        except Exception as e:
            print(f"✗ Error generando historial académico: {e}")
            raise
    
    # ========================================
    # REPORTES DE CURSOS
    # ========================================
    
    def generate_course_report(self, format_type: str = "pdf") -> str:
        """
        Genera un reporte completo de cursos
        """
        try:
            courses = self.course_dao.get_all()
            
            report_data = []
            for course in courses:
                # Obtener estadísticas del curso
                enrollments = self.enrollment_dao.get_by_course(course.id)
                enrolled_count = len(enrollments)
                completed_count = len([e for e in enrollments if e.status == 'completed'])
                avg_grade = sum([e.grade for e in enrollments if e.grade is not None]) / len([e for e in enrollments if e.grade is not None]) if enrollments else 0
                
                report_data.append({
                    'ID': course.id,
                    'Código': course.code,
                    'Nombre': course.name,
                    'Créditos': course.credits,
                    'Instructor': course.instructor or 'Sin asignar',
                    'Semestre': course.semester or 'N/A',
                    'Capacidad': course.capacity,
                    'Inscritos': enrolled_count,
                    'Completados': completed_count,
                    'Promedio': round(avg_grade, 2) if avg_grade > 0 else 'N/A'
                })
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reporte_cursos_{timestamp}"
            
            if format_type.lower() == "pdf":
                return self._generate_pdf_report(report_data, filename, "Reporte de Cursos")
            elif format_type.lower() == "excel":
                return self._generate_excel_report(report_data, filename, "Cursos")
            else:
                return self._generate_csv_report(report_data, filename)
                
        except Exception as e:
            print(f"✗ Error generando reporte de cursos: {e}")
            raise
    
    def generate_course_roster(self, course_id: int, format_type: str = "pdf") -> str:
        """
        Genera la lista de estudiantes inscritos en un curso
        """
        try:
            course = self.course_dao.get_by_id(course_id)
            if not course:
                raise ValueError(f"Curso con ID {course_id} no encontrado")
            
            # Obtener lista de estudiantes
            query = """
            SELECT 
                s.first_name,
                s.last_name,
                s.email,
                e.grade,
                e.status,
                e.enrollment_date
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            WHERE e.course_id = ?
            ORDER BY s.last_name, s.first_name
            """
            
            rows = self.db.execute_query(query, (course_id,))
            roster_data = []
            
            for row in rows:
                roster_data.append({
                    'Nombre': row['first_name'],
                    'Apellido': row['last_name'],
                    'Email': row['email'],
                    'Calificación': row['grade'] if row['grade'] is not None else 'Pendiente',
                    'Estado': row['status'],
                    'Fecha Inscripción': row['enrollment_date']
                })
            
            course_info = {
                'Código': course.code,
                'Nombre': course.name,
                'Instructor': course.instructor or 'Sin asignar',
                'Créditos': course.credits,
                'Capacidad': course.capacity,
                'Inscritos': len(roster_data)
            }
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"lista_{course.code}_{timestamp}"
            
            if format_type.lower() == "pdf":
                return self._generate_roster_pdf(course_info, roster_data, filename)
            else:
                return self._generate_excel_report(roster_data, filename, f"Lista {course.code}")
                
        except Exception as e:
            print(f"✗ Error generando lista de curso: {e}")
            raise
    
    # ========================================
    # REPORTES ESTADÍSTICOS
    # ========================================
    
    def generate_statistics_report(self, format_type: str = "pdf") -> str:
        """
        Genera un reporte con estadísticas generales del sistema
        """
        try:
            # Obtener estadísticas generales
            stats = {}
            
            # Estadísticas de estudiantes
            stats['total_estudiantes'] = self.db.execute_scalar("SELECT COUNT(*) FROM students")
            stats['estudiantes_activos'] = self.db.execute_scalar("SELECT COUNT(*) FROM students WHERE status = 'active'")
            stats['estudiantes_graduados'] = self.db.execute_scalar("SELECT COUNT(*) FROM students WHERE status = 'graduated'")
            
            # Estadísticas de cursos
            stats['total_cursos'] = self.db.execute_scalar("SELECT COUNT(*) FROM courses")
            
            # Estadísticas de inscripciones
            stats['total_inscripciones'] = self.db.execute_scalar("SELECT COUNT(*) FROM enrollments")
            stats['inscripciones_activas'] = self.db.execute_scalar("SELECT COUNT(*) FROM enrollments WHERE status = 'enrolled'")
            stats['cursos_completados'] = self.db.execute_scalar("SELECT COUNT(*) FROM enrollments WHERE status = 'completed'")
            
            # Promedio general de calificaciones
            avg_grade = self.db.execute_scalar("SELECT AVG(grade) FROM enrollments WHERE grade IS NOT NULL")
            stats['promedio_general'] = round(avg_grade, 2) if avg_grade else 0
            
            # Top 5 cursos más populares
            popular_courses = self.db.execute_query("""
                SELECT c.name, c.code, COUNT(e.id) as enrollments
                FROM courses c
                LEFT JOIN enrollments e ON c.id = e.course_id
                GROUP BY c.id, c.name, c.code
                ORDER BY enrollments DESC
                LIMIT 5
            """)
            
            # Distribución de calificaciones
            grade_distribution = self.db.execute_query("""
                SELECT 
                    CASE 
                        WHEN grade >= 90 THEN 'A (90-100)'
                        WHEN grade >= 80 THEN 'B (80-89)'
                        WHEN grade >= 70 THEN 'C (70-79)'
                        WHEN grade >= 60 THEN 'D (60-69)'
                        WHEN grade < 60 THEN 'F (0-59)'
                    END as grade_range,
                    COUNT(*) as count
                FROM enrollments 
                WHERE grade IS NOT NULL
                GROUP BY grade_range
                ORDER BY grade_range
            """)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"estadisticas_{timestamp}"
            
            if format_type.lower() == "pdf":
                return self._generate_statistics_pdf(stats, popular_courses, grade_distribution, filename)
            else:
                # Para Excel/CSV, crear estructura de datos tabular
                stats_data = [{'Métrica': k, 'Valor': v} for k, v in stats.items()]
                return self._generate_excel_report(stats_data, filename, "Estadísticas")
                
        except Exception as e:
            print(f"✗ Error generando reporte estadístico: {e}")
            raise
    
    # ========================================
    # MÉTODOS PRIVADOS PARA GENERACIÓN DE ARCHIVOS
    # ========================================
    
    def _generate_pdf_report(self, data: List[Dict[str, Any]], filename: str, title: str) -> str:
        """Genera un reporte en formato PDF"""
        if not REPORTLAB_AVAILABLE:
            raise ImportError("ReportLab no está disponible. Instalar con: pip install reportlab")
        
        filepath = self.output_dir / f"{filename}.pdf"
        doc = SimpleDocTemplate(str(filepath), pagesize=A4)
        story = []
        
        # Título
        story.append(Paragraph(title, self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Información de generación
        story.append(Paragraph(f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M')}", self.styles['Normal']))
        story.append(Spacer(1, 20))
        
        if data:
            # Crear tabla con los datos
            headers = list(data[0].keys())
            table_data = [headers]
            
            for row in data:
                table_data.append([str(row[header]) for header in headers])
            
            # Crear tabla
            table = Table(table_data, repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
        else:
            story.append(Paragraph("No se encontraron datos para el reporte.", self.styles['Normal']))
        
        doc.build(story)
        print(f"✓ Reporte PDF generado: {filepath}")
        return str(filepath)
    
    def _generate_excel_report(self, data: List[Dict[str, Any]], filename: str, sheet_name: str) -> str:
        """Genera un reporte en formato Excel"""
        if not PANDAS_AVAILABLE:
            # Fallback a CSV si pandas no está disponible
            return self._generate_csv_report(data, filename)
        
        filepath = self.output_dir / f"{filename}.xlsx"
        df = pd.DataFrame(data)
        
        with pd.ExcelWriter(str(filepath), engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            # Agregar información de metadatos en una hoja separada
            metadata = pd.DataFrame([
                {'Campo': 'Fecha de Generación', 'Valor': datetime.now().strftime('%d/%m/%Y %H:%M')},
                {'Campo': 'Total de Registros', 'Valor': len(data)},
                {'Campo': 'Sistema', 'Valor': 'Sistema de Gestión Educativa'}
            ])
            metadata.to_excel(writer, sheet_name='Información', index=False)
        
        print(f"✓ Reporte Excel generado: {filepath}")
        return str(filepath)
    
    def _generate_csv_report(self, data: List[Dict[str, Any]], filename: str) -> str:
        """Genera un reporte en formato CSV"""
        filepath = self.output_dir / f"{filename}.csv"
        
        if data:
            import csv
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        
        print(f"✓ Reporte CSV generado: {filepath}")
        return str(filepath)
    
    def _generate_html_report(self, data: List[Dict[str, Any]], filename: str, title: str) -> str:
        """Genera un reporte en formato HTML"""
        filepath = self.output_dir / f"{filename}.html"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; text-align: center; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
                .info {{ margin-bottom: 20px; color: #666; }}
            </style>
        </head>
        <body>
            <h1>{title}</h1>
            <div class="info">
                <p>Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
                <p>Total de registros: {len(data)}</p>
            </div>
        """
        
        if data:
            html_content += "<table><thead><tr>"
            for header in data[0].keys():
                html_content += f"<th>{header}</th>"
            html_content += "</tr></thead><tbody>"
            
            for row in data:
                html_content += "<tr>"
                for value in row.values():
                    html_content += f"<td>{value}</td>"
                html_content += "</tr>"
            
            html_content += "</tbody></table>"
        else:
            html_content += "<p>No se encontraron datos para el reporte.</p>"
        
        html_content += "</body></html>"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ Reporte HTML generado: {filepath}")
        return str(filepath)
    
    def _generate_transcript_pdf(self, student_info: Dict[str, Any], 
                                transcript_data: List[Dict[str, Any]], filename: str) -> str:
        """Genera un historial académico en PDF"""
        if not REPORTLAB_AVAILABLE:
            raise ImportError("ReportLab no está disponible")
        
        filepath = self.output_dir / f"{filename}.pdf"
        doc = SimpleDocTemplate(str(filepath), pagesize=A4)
        story = []
        
        # Título
        story.append(Paragraph("HISTORIAL ACADÉMICO", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Información del estudiante
        story.append(Paragraph("INFORMACIÓN DEL ESTUDIANTE", self.styles['CustomHeading']))
        for key, value in student_info.items():
            story.append(Paragraph(f"<b>{key}:</b> {value}", self.styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Historial de cursos
        story.append(Paragraph("HISTORIAL DE CURSOS", self.styles['CustomHeading']))
        
        if transcript_data:
            headers = list(transcript_data[0].keys())
            table_data = [headers]
            
            for row in transcript_data:
                table_data.append([str(row[header]) for header in headers])
            
            table = Table(table_data, repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 9),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
        
        doc.build(story)
        print(f"✓ Historial académico PDF generado: {filepath}")
        return str(filepath)
    
    def _generate_roster_pdf(self, course_info: Dict[str, Any], 
                            roster_data: List[Dict[str, Any]], filename: str) -> str:
        """Genera una lista de curso en PDF"""
        if not REPORTLAB_AVAILABLE:
            raise ImportError("ReportLab no está disponible")
        
        filepath = self.output_dir / f"{filename}.pdf"
        doc = SimpleDocTemplate(str(filepath), pagesize=A4)
        story = []
        
        # Título
        story.append(Paragraph("LISTA DE ESTUDIANTES", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Información del curso
        story.append(Paragraph("INFORMACIÓN DEL CURSO", self.styles['CustomHeading']))
        for key, value in course_info.items():
            story.append(Paragraph(f"<b>{key}:</b> {value}", self.styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Lista de estudiantes
        story.append(Paragraph("ESTUDIANTES INSCRITOS", self.styles['CustomHeading']))
        
        if roster_data:
            headers = list(roster_data[0].keys())
            table_data = [headers]
            
            for row in roster_data:
                table_data.append([str(row[header]) for header in headers])
            
            table = Table(table_data, repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.green),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 9),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
        
        doc.build(story)
        print(f"✓ Lista de curso PDF generada: {filepath}")
        return str(filepath)
    
    def _generate_statistics_pdf(self, stats: Dict[str, Any], popular_courses: List, 
                                grade_distribution: List, filename: str) -> str:
        """Genera un reporte estadístico en PDF"""
        if not REPORTLAB_AVAILABLE:
            raise ImportError("ReportLab no está disponible")
        
        filepath = self.output_dir / f"{filename}.pdf"
        doc = SimpleDocTemplate(str(filepath), pagesize=A4)
        story = []
        
        # Título
        story.append(Paragraph("REPORTE ESTADÍSTICO", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Estadísticas generales
        story.append(Paragraph("ESTADÍSTICAS GENERALES", self.styles['CustomHeading']))
        for key, value in stats.items():
            story.append(Paragraph(f"<b>{key.replace('_', ' ').title()}:</b> {value}", self.styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Cursos más populares
        story.append(Paragraph("CURSOS MÁS POPULARES", self.styles['CustomHeading']))
        if popular_courses:
            course_table = [['Curso', 'Código', 'Inscripciones']]
            for course in popular_courses:
                course_table.append([course['name'], course['code'], str(course['enrollments'])])
            
            table = Table(course_table)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
            story.append(Spacer(1, 20))
        
        # Distribución de calificaciones
        if grade_distribution:
            story.append(Paragraph("DISTRIBUCIÓN DE CALIFICACIONES", self.styles['CustomHeading']))
            grade_table = [['Rango de Calificaciones', 'Cantidad']]
            for grade in grade_distribution:
                grade_table.append([grade['grade_range'], str(grade['count'])])
            
            table = Table(grade_table)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
        
        doc.build(story)
        print(f"✓ Reporte estadístico PDF generado: {filepath}")
        return str(filepath)
    
    # ========================================
    # UTILIDADES
    # ========================================
    
    def get_available_formats(self) -> List[str]:
        """Retorna los formatos disponibles según las librerías instaladas"""
        formats = ["csv", "html"]
        if PANDAS_AVAILABLE:
            formats.append("excel")
        if REPORTLAB_AVAILABLE:
            formats.append("pdf")
        return formats
    
    def cleanup_old_reports(self, days_old: int = 30) -> int:
        """Elimina reportes antiguos"""
        import time
        cutoff_time = time.time() - (days_old * 24 * 60 * 60)
        deleted_count = 0
        
        for file_path in self.output_dir.iterdir():
            if file_path.is_file() and file_path.stat().st_mtime < cutoff_time:
                file_path.unlink()
                deleted_count += 1
        
        print(f"✓ Eliminados {deleted_count} reportes antiguos")
        return deleted_count
