 # @jwt_required()
    # @blp.response(200,StudentAndAssessmentSchema)
    # def get(self,student_assessment_id):
    #     student_assessment = StudentsAssessments.query.get(student_assessment_id)

    #     return student_assessment

    # # @jwt_required()
    # def delete(self, student_assessment_id):
    #     student_assessment = StudentsAssessments.query.get(student_assessment_id)

    #     db.session.delete(student_assessment)
    #     db.session.commit()

    #     return {"message": "This student_assessment was deleted"}