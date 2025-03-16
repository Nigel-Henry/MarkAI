// frontend/src/utils/apiRateLimiter.js

const ApiRateLimiter = {
    queue: [],
    maxRequests: 10,
    interval: 60000,

    addRequest(request) {
        this.queue.push({
            timestamp: Date.now(),
            request
        });
        this._cleanup();
        return this.queue.length < this.maxRequests;
    },

    _cleanup() {
        const now = Date.now();
        this.queue = this.queue.filter(
            req => now - req.timestamp < this.interval
        );
    }
};

export default ApiRateLimiter;