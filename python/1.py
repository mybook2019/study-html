def sync_itms_realtime(data ):
    collection = db['res-new']
    # 插入数据到MongoDB
    collection.insert_one(data)

    # 同步到另一个系统
    sync_result = sync_to_system(data)

    # 根据同步结果，更新MongoDB中的sync字段
    if sync_result == "同步成功":
        collection.update_one(
            {"_id": data["_id"]},
            {"$set": {"sync": True, "sync_result": sync_result}}
        )
    else:
        collection.update_one(
            {"_id": data["_id"]},
            {"$set": {"sync": False, "sync_result": sync_result}}
        )
        logger.error(f"Failed to sync item system: {str(sync_result)}")
        return False, f"Failed to sync item system: {str(sync_result)}", 500

    lotSnCode = data["lotSnCode"]
    # 将 lotSnCode 放入 Redis Set
    redis_client.sadd(REDIS_SET_KEY, lotSnCode)

    return True, "",200



def sync_data_offline(data):
    if data["isPass"] == True:
        # Add insert time
        data['insert_time'] = datetime.utcnow()
        # Include testFrameidNo in the document
        # Insert data into MongoDB
        collection.insert_one(data)

        lotSnCode = data["lotSnCode"]

        # 将 lotSnCode 放入 Redis Set
        redis_client.sadd(REDIS_SET_KEY, lotSnCode)
    
    return True, "",200