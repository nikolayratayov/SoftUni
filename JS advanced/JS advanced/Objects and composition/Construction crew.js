function result(worker){
    if (worker.dizziness){
        let need = 0.1 * worker.weight * worker.experience;
        worker.levelOfHydrated += need;
        worker.dizziness = false;
    }
    return worker
}