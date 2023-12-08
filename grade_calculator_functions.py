from typing import List

class GradeCalculator:
    """
    Class to calculate grades based on scores.
    """

    def __init__(self, student_names: List[str]) -> None:
        """
        Initialize the GradeCalculator instance.

        Args:
            student_names (List[str]): List of student names.
        """
        self.student_names = student_names
        self.scores = []

    def input_scores(self, scores_str: str) -> None:
        """
        Input student scores.

        Args:
            scores_str (str): String containing student scores separated by space.

        Raises:
            ValueError: If not enough scores are provided.
        """
        all_scores = list(map(int, scores_str.split()))
        if len(all_scores) >= len(self.student_names):
            self.scores = all_scores[:len(self.student_names)]
        else:
            raise ValueError("Not enough scores provided.")

    def letter_grade(self, score: int, best_score: int) -> str:
        """
        Calculate letter grade based on the score and the best score.

        Args:
            score (int): The student's score.
            best_score (int): The best score among all students.

        Returns:
            str: The letter grade.
        """
        if score >= best_score - 10:
            return 'A'
        elif score >= best_score - 20:
            return 'B'
        elif score >= best_score - 30:
            return 'C'
        elif score >= best_score - 40:
            return 'D'
        else:
            return 'F'

    def calculate_grades(self) -> List[str]:
        """
        Calculate grades for all students.

        Returns:
            List[str]: List of strings containing student information and grades.
        """
        best_score = max(self.scores)
        result = []
        for i, (name, score) in enumerate(zip(self.student_names, self.scores)):
            grade = self.letter_grade(score, best_score)
            result.append(f"{name}'s score is {score} and grade is {grade}")
        return result



