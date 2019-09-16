// pages/search/search.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    winHeight: "",//窗口高度
    scrollTop: 0,
    hotWords: [],
    showHotWords: [],  //随机显示六个热词
    showSearchContent: false,
    searchValue: '',
    searchRes: {},
    historyWords: []
  },

  searchInput: function (event) {  //手动清空搜索栏关闭搜索容器
    this.setData({
      searchValue: event.detail.value
    });
    if (event.detail.value.length === 0) {
      this.setData({
        showSearchContent: false
      });
    }
  },

  clearInput: function () { //清空搜索栏关闭搜索容器
    this.setData({
      searchValue: '',
      showSearchContent: false
    });
  },

  search: function (word) {
    var that = this;
    wx.showLoading({
      title: '搜索中',
      mask: true
    });
    wx.request({
      url: app.buildUrl("/book/search/"),
      header: app.getRequestHeader(),
      data: {
        keyword: that.data.searchValue,
      },
      method: 'POST',
      success: function (res) {
        that.setData({
          showSearchContent: true,
          searchRes: res.data,
          scrollTop: 0
        });
        wx.hideLoading();
      }
    })
  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    //  高度自适应
    wx.getSystemInfo({
      success: (res) => {
        var clientHeight = res.windowHeight,
          clientWidth = res.windowWidth,
          rpxR = 750 / clientWidth;
        var calc = clientHeight * rpxR - 140;
        this.setData({
          winHeight: calc
        });
      }
    });

  }
})