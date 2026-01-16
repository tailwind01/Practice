interface TTL{
    value: number;
    timer: ReturnType<typeof setTimeout>;
}

class TimeLimitedCache {
    memory = new Map<number, TTL>()
    set(key: number, value: number, duration: number): boolean {
        const present=this.memory.has(key)
        if (present) clearTimeout(this.memory.get(key).timer)
        this.memory.set(key,{value,timer: setTimeout(() => this.memory.delete(key), duration)})
        return present
        
    }
    
    get(key: number): number {
        return this.memory.has(key) ? this.memory.get(key).value : -1
    }
    
    count(): number {
        return this.memory.size
    }
}
