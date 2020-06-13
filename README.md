## 切入mongodb環境
- mongo
### 顯示目前操作的database
- db
### 檢視資料庫
- show dbs
### 切換資料庫
- use database
### 檢視collections
- show collections 
### 顯示 collections資料筆數
- db.products.count()
### 回傳所有資料
- db.products.find()
- db.products.find().pretty()
### 找出_id為ac3的資料
- db.products.find( { _id : "ac3" } ) 
### 找出price大於等於200的資料
- db.products.find( { price: {$gte:200 } } )  
### 找出price大於200的資料
- db.products.find( { price: {$gt:200 } } )  
### lte  (小於等於)
- db.products.find( { price: {$lte:200 } } )
### $lt    (小於)
- db.products.find( { price: {$lt:200 } } ) 
### Insert
- db.people.insert({name:"alice",type:"student",age:20,array:[1,2,3,4,5]})
### update 
#### (若沒有使用$set的指令指定更新哪個欄位 ，update指令會將整筆資料進行更動(沒加上的欄位就直接清掉了)，會造成資料遺失)
- db.people.update( { "type" : "student"},{ "type" : "engineer"},{ multi:true} )
- db.people.update( { "name": "alice" },{ $set : { age :30} })
### import JSON
- (在cmd下面輸入) mongoimport --jsonArray --db a_dbname --collection a_collectname --file C:\...\...\.json
