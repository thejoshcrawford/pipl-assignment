const store = {
    csfr_token: '',
    origin: window.location.origin,
    polls: [],
    activePoll: {},
    newPoll: {
        title: '',
        options: [
            { title: '' },
        ]
    }
}

const Home = {
    delimiters: ['{', '}'],
    template: `
    <div>
        <h1>Pipl Polls</h1>
        <router-link lass="btn btn-primary" v-bind:to="{ name: 'create' }">Create New Poll</router-link>
        <hr>
        <h2>Recent Polls</h2>
        <ul class="list-group">
            <li class="list-group-item" v-for="poll in polls">
                <div class="row">
                    <div class="col">{poll.title}</div>
                    <div class="col">
                        <router-link v-bind:to="{name: 'poll', params: {pollUrl: poll.url}}">{origin}/poll/{poll.url}</router-link>
                    </div>
                </div>
            </li>
        </ul>
    </div>
    `,
    data: function () {
        return store
    },
    mounted: function () {
        this.getPolls()
    },
    methods: {
        addOption: function () {
            this.newPoll.options.push({ title: '' })
        },
        getPolls: function () {
            this.$http.get('/api/poll')
                .then(function (response) {
                    let polls = response.body
                    polls = polls.sort(function (a, b) {
                        if (a.date === b.date) {
                            return 0;
                        }

                        if (b.date === null) {
                            return -1
                        }

                        if (a.date === null) {
                            return 1
                        }

                        if (a.date > b.date) {
                            return -1
                        }

                        return 1
                    })
                    this.polls = polls.slice(0, 10)
                })
                .catch(function (err) {
                    console.log(err)
                })
        },
    }
}

const Create = {
    delimiters: ['{', '}'],
    template: `
    <div>
        <h1>Pipl Polls</h1>
        <router-link lass="btn btn-primary" v-bind:to="{ name: 'home' }">Home</router-link>
        <hr>
        <h2>Create a Poll</h2>
        <div class="form-group">
            <label for="poll-title">Title</label>
            <input type="text" class="form-control" id="poll-title" aria-describedby="titleHelp"
                v-model="newPoll.title" placeholder="Enter title">
        </div>
        <div class="form-group">
            <label>Options</label>
            <input type="text" class="form-control mt-1" aria-describedby="optionHelp"
                v-for="(option, index) in newPoll.options" v-bind:key="index" v-model="option.title"
                placeholder="Enter poll option">
        </div>
        <div class="form-group">
            <button type="button" class="btn btn-primary" v-on:click="addOption">Add Option</button>
        </div>
        <button type="submit" class="btn btn-primary" v-on:click="createPoll">Create Poll</button>
    </div>
    `,
    data: function () {
        return store
    },
    methods: {
        addOption: function () {
            this.newPoll.options.push({ title: '' })
        },
        createPoll: function () {
            var vm = this;
            this.$http.post('/api/poll/',
                this.newPoll,
                {
                    headers: {
                        'X-CSRFToken': this.csfr_token
                    }
                })
                .then(function (response) {
                    let poll = response.body;

                    // my attempt at bulk saving options, in progress
                    // let options = []
                    // vm.newPoll.options.forEach(function (option) {
                    //     option['poll']
                    //     options.push(option)
                    // })

                    // vm.$http.post("/api/poll_option/",
                    //     options,
                    //     {
                    //         headers: {
                    //             'X-CSRFToken': vm.csfr_token
                    //         }
                    //     })
                    //     .then(function (res) {
                    //         console.log(res);
                    //     })
                    //     .catch(function (err) {
                    //         console.log(err);
                    //     })

                    vm.newPoll.options.forEach(function (option) {
                        option['poll'] = poll.id
                        vm.$http.post('/api/poll_option/',
                            option,
                            {
                                headers: {
                                    'X-CSRFToken': vm.csfr_token
                                }
                            })
                            .then(function (res) {
                                console.log(res);
                            })
                            .catch(function (err) {
                                // show errors
                                console.log(err);
                            })
                    })

                    // add poll to list
                    this.polls.splice(0, 0, poll)

                    // reset
                    this.newPoll = {
                        title: '',
                        options: [
                            { title: '' },
                        ]
                    }

                    // go to poll
                    router.push({ name: 'poll', params: { pollUrl: poll.url } })
                })
                .catch(function (err) {
                    console.log(err);
                })
        },
    }
}

const Poll = {
    delimiters: ['{', '}'],
    template: `
    <div>
        <h1>Pipl Polls</h1>
        <router-link lass="btn btn-primary" v-bind:to="{ name: 'home' }">Home</router-link>
        <hr>
        <h1>{activePoll.title}</h1>
        <ul class="list-group">
            <li class="list-group-item" v-for="option in activePoll.options">
                <div class="row">
                    <div class="col">{option.title}</div>
                    <div v-if="activePoll.voted==false" class="col"><button class="btn btn-primary" v-on:click='vote(option.id)'>Vote for this one</button></div>
                    <div v-if="activePoll.voted==true" class="col">{option.count}</div>
                </div>
            </li>
        </ul>
    </div>`,
    data: function () {
        return store
    },
    mounted: function () {
        this.getPoll()
    },
    methods: {
        getPoll: function () {
            this.$http.get('/api/poll/' + this.$route.params.pollUrl)
                .then(function (response) {
                    this.activePoll = response.body
                })
                .catch(function (err) {
                    console.log(err);
                }
                )
        },
        vote: function (optionId) {
            this.$http.post('/api/poll_response/',
                { 'poll_option': optionId },
                {
                    headers: {
                        'X-CSRFToken': this.csfr_token
                    }
                })
                .then(function (response) {
                    console.log(response)
                    let option = this.activePoll.options.filter(function (o) {
                        return o.id === optionId;
                    })[0]
                    option.count++
                })
                .catch(function (err) {
                    console.log(err);
                }
                )
            this.activePoll.voted = true;
        }
    }
}

const routes = [
    { name: 'home', path: '/', component: Home },
    { name: 'create', path: '/create', component: Create },
    { name: 'poll', path: '/poll/:pollUrl', component: Poll },
]

const router = new VueRouter({
    routes: routes,
    mode: 'history'
})

const app = new Vue({
    router: router,
    delimiters: ['{', '}'],
    data: function () {
        return store
    },
    mounted: function () {
        this.csfr_token = document.cookie.split('; ').filter(function (val) {
            return val.substring(0, 10) == 'csrftoken=';
        })[0].slice(10)
    },
}).$mount('#app'); 