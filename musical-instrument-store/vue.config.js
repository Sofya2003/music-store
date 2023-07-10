const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true
})
// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   /* your config */
//   configureWebpack: {
//       optimization: {
//           runtimeChunk: 'single',
//       },
//   },
//   devServer: {
//       // we need this for apollo to work properly
//       proxy: `https://${process.env.SANDBOX_HOSTNAME}/`,
//       host: '0.0.0.0',
//       allowedHosts: 'all',
//   },
// });
