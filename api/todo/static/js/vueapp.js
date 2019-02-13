new Vue({
    el: '#vuecrud',
    delimiters: ['${', '}'],
    data: {
        tasks: [],
        loading: false,
        currentTask: {},
        message: null,
        newTask: {
            'description': null,
            'date': null,
            'time': null,
            'category': null,
            'priority': null
        },
    },

    mounted: function () {
        this.getTasks();
    },

    methods: {

        getTasks: function () {
            this.loading = true;
            this.$http.get('api/v1/tasks')
                .then((response) => {
                    this.tasks = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })

        },
        getTask: function (id) {
            this.loading = true;
            this.$http.get(`api/v1/tasks/${id}`)
                .then((response) => {
                    this.currentTask = response.data;
                    $("#editTaskModal").modal('show');
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addTask: function () {
            this.loading = true;
            this.$http.post('/api/v1/tasks', this.newTask)
                .then((response) => {
                    this.loading = false;
                    $("#addTaskModal").modal('hide');
                    this.getTasks();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        updateTask: function () {
            this.loading = true;
            this.$http.put(`api/v1/tasks/${this.currentTask.id}`, this.currentTask)
                .then((response) => {
                    this.loading = false;
                    this.currentTask = response.data;
                    $("#editTaskModal").modal('hide');
                    this.getTasks();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        deleteTask: function (id) {
            this.loading = true;
            this.$http.delete(`api/v1/tasks/${id}`)
                .then((response) => {
                    this.loading = false;
                    this.getTasks();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        }
    }
});