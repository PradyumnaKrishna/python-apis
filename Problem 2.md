Write a web application (only API, no UI) in Python 3 that can be used as a scheduler. The server will maintain fixed
slots of 1 hour starting from 12 AM (so, slots would be 0, 1, 2, .. 23 where each number represents the starting hour of
the slot) and would accept bookings. Each slot can have maximum 2 bookings. Subsequent requests for the same slot would
fail unless a booking is canceled. Implement two endpoints:

POST /booking - Given a name and slot number, save the details if space is available in the slot, else return error.
POST /cancel - Given a name and slot number, delete the booking if available else return error. GET /booking - Show all
bookings

Eg:

Input:

```json
POST /booking {
  "slot": 1,
  "name": "John"
}
```

Output:

```json
{
  "status": "confirmed"
}
```

Input:

```json
POST /booking {
  "slot": 2,
  "name": "Jane"
}
```

Output:

```json
{
  "status": "confirmed"
}
```

Input

```json
POST /booking {
  "slot": 2,
  "name": "Diana"
}
```

Output:

```json
{
  "status": "confirmed"
}
```

Input:

```json
POST /booking {
  "slot": 2,
  "name": "Riker"
}
```

Output:

```json
{
  "status": "slot full, unable to save booking for Riker in slot 2"
}
```

Input:

```json
GET /booking
```

Output:

```json
[
  {
    "slot": 1,
    "name": "John"
  },
  {
    "slot": 2,
    "name": [
      "Diana",
      "Jane"
    ]
  }
]
```

Input

```json
POST /cancel {
  "slot": 2,
  "name": "Diana"
}
```

Output:

```json{
"status": "canceled booking for Diana in slot 2"
}
```

Input

```json
POST /booking {
  "slot": 2,
  "name": "Riker"
}
```

Output:

```
{
"status": "confirmed booking for Riker in slot 2"
}
```

Input:

```json
POST /cancel {
  "slot": 2,
  "name": "Diana"
}
```

Output:

```json
{
  "status": "no booking for the name Diana in slot 2"
}
```

Input:

```json
GET /booking
```

```json
[
  {
    "slot": 1,
    "name": "John"
  },
  {
    "slot": 2,
    "name": [
      "Jane",
      "Riker"
    ]
  }
]
```
