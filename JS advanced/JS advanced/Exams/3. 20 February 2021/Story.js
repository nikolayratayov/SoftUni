class Story {
    #comments
    #likes
    constructor(title, creator){
        this.title = title;
        this.creator = creator;
        this.#comments = [];
        this.#likes = [];
    }

    get likes(){
        if (this.#likes.length == 0){
            return `${this.title} has 0 likes`
        }
        else if (this.#likes.length == 1){
            return `${this.#likes[0]} likes this story!`
        }
        return `${this.#likes[0]} and ${this.#likes.length - 1} others like this story!`
    }

    like (username){
        if(this.#likes.includes(username)){
            throw new Error('You can\'t like the same story twice!"')
        }
        if (this.creator == username){
            throw new Error('You can\'t like your own story!')
        }
        this.#likes.push(username);
        return `${username} liked ${this.title}!`
    }

    dislike (username){
        if (!this.#likes.includes(username)){throw new Error('You can\'t dislike this story!')}
        let idx = this.#likes.indexOf(username);
        this.#likes.splice(idx, 1);
        return `${username} disliked ${this.title}`
    }

    comment (username, content, id){
        if (id == undefined){
            let new_id = this.#comments.length + 1;
            let new_comment = {'Id': new_id, 'Username': username, 'Content': content, 'Replies': []};
            this.#comments.push(new_comment)
            return `${username} commented on ${this.title}`
        }
        for (let com of this.#comments){
            if (com.Id == id){
                let new_reply_id = com.Replies.length + 1;
                let new_reply = {'Id': new_reply_id, 'Username': username, 'Content': content}
                com.Replies.push(new_reply);
                return 'You replied successfully'
            }
        }
        let new_id = this.#comments.length + 1;
        let new_comment = {'Id': new_id, 'Username': username, 'Content': content, 'Replies': []};
        this.#comments.push(new_comment)
        return `${username} commented on ${this.title}`
    }

    toString(type){
        let sorted_comments;
        if (type == 'asc'){
            sorted_comments = this.#comments.sort((a, b) => {return a.Id - b.Id});
        }
        else if (type == 'desc'){
            sorted_comments = this.#comments.sort((a, b) => {return b.Id - a.Id});
        }
        else{
            sorted_comments = this.#comments.sort((a, b) => a.Username.localeCompare(b.Username));
        }
        let res = '';
        res += `Title: ${this.title}\n`;
        res += `Creator: ${this.creator}\n`;
        res += `Likes: ${this.#likes.length}\n`;
        res += `Comments:\n`;
        if (this.#comments.length > 0){
            for (let com of sorted_comments){
                res += `-- ${com.Id}. ${com.Username}: ${com.Content}\n`;
                if (com.Replies.length > 0){
                    let sorted_replies;
                    if (type == 'asc'){
                        sorted_replies = com.Replies.sort((a, b) => {return a.Id - b.Id});
                    }
                    else if (type == 'desc'){
                        sorted_replies = com.Replies.sort((a, b) => {return b.Id - a.Id});
                    }
                    else{
                        sorted_replies = com.Replies.sort((a, b) => a.Username.localeCompare(b.Username));
                    }
                    for (let reply of sorted_replies){
                        res += `--- ${com.Id}.${reply.Id}. ${reply.Username}: ${reply.Content}\n`
                    }
                }
            }
        }
        return res.substring(0, res.length - 1)
    }
}
