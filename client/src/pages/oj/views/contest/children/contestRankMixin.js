import api from '@oj/api'
import ScreenFull from '@admin/components/ScreenFull.vue'
import { mapGetters, mapState } from 'vuex'
import { types } from '@/store'
import { CONTEST_STATUS } from '@/utils/constants'

export default {
  data () {
    return {
      loading: false
    }
  },
  components: {
    ScreenFull
  },
  methods: {
    getContestRankData (page = 1, refresh = false) {
      let offset = (page - 1) * this.limit
      if (!refresh) {
        this.loading = true
      }
      let params = {
        offset,
        limit: this.limit,
        contest_id: this.$route.params.contestID,
        force_refresh: this.forceUpdate ? '1' : '0'
      }
      api.getContestRank(params).then(res => {
        if (!refresh) {
          this.loading = false
        }
        this.total = res.data.data.total
        this.applyToTable(res.data.data.results)
      })
    },
    handleAutoRefresh (status) {
      if (status === true) {
        this.refreshFunc = setInterval(() => {
          this.page = 1
          this.getContestRankData(1, true)
        }, 10000)
      } else {
        clearInterval(this.refreshFunc)
      }
    }
  },
  computed: {
    ...mapGetters(['isContestAdmin']),
    ...mapState({
      'contest': state => state.contest.contest,
      'contestProblems': state => state.contest.contestProblems
    }),
    showMenu: {
      get () {
        return this.$store.state.contest.itemVisible.menu
      },
      set (value) {
        this.$store.commit(types.CHANGE_CONTEST_ITEM_VISIBLE, {menu: value})
        this.$nextTick(() => {
          this.$refs.tableRank.handleResize()
        })
      }
    },
    showTeamMembers: {
      get () {
        return this.$store.state.contest.itemVisible.realName
      },
      set (value) {
        this.$store.commit(types.CHANGE_CONTEST_ITEM_VISIBLE, {realName: value})
        if (value) {
          this.columns.splice(2, 0, {
            title: 'Team Members',
            align: 'center',
            fixed: 'left',
            minWidth: 220,
            render: (h, {row}) => {
              return h('span', row.user.team_members.map(member => member.name).join(', ') + ' (' + row.user.username + ')')
            }
          })
        } else {
          this.columns.splice(2, 1)
        }
      }
    },
    forceUpdate: {
      get () {
        return this.$store.state.contest.forceUpdate
      },
      set (value) {
        this.$store.commit(types.CHANGE_RANK_FORCE_UPDATE, {value: value})
      }
    },
    limit: {
      get () {
        return this.$store.state.contest.rankLimit
      },
      set (value) {
        this.$store.commit(types.CHANGE_CONTEST_RANK_LIMIT, {rankLimit: value})
      }
    },
    refreshDisabled () {
      return this.contest.status === CONTEST_STATUS.ENDED
    }
  },
  beforeDestroy () {
    clearInterval(this.refreshFunc)
  }
}
