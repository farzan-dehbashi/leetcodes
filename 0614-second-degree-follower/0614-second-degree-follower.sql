select followee as follower, count(distinct follower) as num
from Follow
where followee in (select follower from Follow)
group by followee