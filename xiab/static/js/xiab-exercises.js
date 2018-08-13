var vm = new Vue({
    el: '#exercise-app',
    data: {
        questionIndex: 0,
        questions: questions,
    }, methods: {
        checkAnswer: function() {
            var currentQuestion = this.questions[this.questionIndex]
            currentQuestion.result = (currentQuestion.userAnswer == currentQuestion.answer);
        }
    }
});