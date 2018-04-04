(function(){$.ajaxSetup({beforeSend:function(e,t){/^http:.*/.test(t.url)||/^https:.*/.test(t.url)||e.setRequestHeader("X-CSRFToken",function(e){var t,n,o,u=null
if(document.cookie&&""!=document.cookie)for(t=document.cookie.split(";"),n=0;n<t.length;n++)if((o=jQuery.trim(t[n])).substring(0,e.length+1)==e+"="){u=decodeURIComponent(o.substring(e.length+1))
break}return u}("csrftoken"))}})}).call(this)
