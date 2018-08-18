var vm = new Vue({
    el: '#exercise-app',
    data: {
        questionIndex: 0,
        questions: questions,
        currentQuestion: questions[0],
    }, methods: {
        disableSubmission: function() {
            // return this.currentQuestion.userAnswer === "";
            return false;
        },
        changeQuestion: function(n) {
            this.questionIndex += n;
            this.currentQuestion = this.questions[this.questionIndex];
        },
        checkAnswer: function() {
            var result;
            if (this.currentQuestion.type === 'numeric') {
                result = parseFloat(this.currentQuestion.userAnswer) == this.currentQuestion.answer;
            } else if (this.currentQuestion.type === 'multiple_choice') {
                result = this.currentQuestion.userAnswer === this.currentQuestion.answer;
            }

            this.currentQuestion.result = result;
        },
    }
});