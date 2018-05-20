##  场景1：修改代码后，编译构建，发布，实现业务代码升级
#### 流程
>>>
首先：获取环境变量（版本、服务名称等）
其次：拼装URL
其次：查询当前服务部署状态是否正常，若不正常，报错退出【问题：当前接口未开放】
其次：调用部署接口
最后：调用查询接口，查看当前是否正常
>>>

#### 依赖变量
*  FUXI_VERSION：服务名称【必选】
*  TITAN_SERVICE：容器服务名称【必选】
*  TITAN_INST_NAME：容器实例名称【必选】
*  TITAN_APP_NAME：容器应用名称【必选】
*  TITAM_TEAM_NAME：容器组【必选】
*  IMAGE_TAG：容器tag【可选】
*  ENVS：容器环境变量【必选】（当前不知道环境变量是否存在）

##  场景2：使用已有容器包部署
>>>
首先：获取环境变量，以及当前容器的地址版本
其次：参照场景1部署
>>>

##  场景3：配置项变更
>>>
同场景1
>>>

