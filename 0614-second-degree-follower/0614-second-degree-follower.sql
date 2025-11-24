select followee as follower, count(distinct follower) as num
from Follow
where followee in(select follower from follow)
group by followee