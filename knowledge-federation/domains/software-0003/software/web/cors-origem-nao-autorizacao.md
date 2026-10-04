---
id: software.web.cors.000001
tipo: conceito
dominio: software
subdominio: web
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [CORS, Cross-Origin Resource Sharing, política de mesma origem]
lote: software-seguranca-0003
---

# CORS controla compartilhamento no navegador, não autorização

## Em uma frase
CORS é um protocolo de navegador que permite a um servidor declarar quais origens podem ler determinadas respostas cross-origin; ele não é um controle de acesso para o servidor.

## Por que importa
Uma configuração CORS incorreta pode expor respostas a scripts executados em origens não autorizadas, especialmente quando credenciais estão envolvidas. O equívoco inverso também é comum: desenvolvedores esperam que CORS impeça chamadas feitas por clientes que não sejam navegadores. A autenticação e a autorização de cada operação continuam sendo responsabilidades do servidor.

## Como funciona
O navegador avalia os cabeçalhos CORS da resposta para decidir se disponibiliza o resultado ao código da página. Para certas requisições, envia antes uma requisição `OPTIONS` de preflight; outras podem ser enviadas sem esse passo. Com modo de credenciais, o servidor precisa permitir uma origem explícita e retornar `Access-Control-Allow-Credentials: true`; `Access-Control-Allow-Origin: *` não pode liberar a resposta credenciada. Se a resposta varia conforme o `Origin`, `Vary: Origin` ajuda caches a não misturar representações. A lista de origens deve ser comparada com uma allow-list exata, não refletida cegamente do cabeçalho recebido.

## Exemplo
Um frontend confiável em `https://app.example` acessa uma API em outra origem. A API valida essa origem contra configuração conhecida e retorna `Access-Control-Allow-Origin: https://app.example`. Se cookies cross-origin forem necessários, a política explícita de credenciais deve ser configurada e testada. Uma aplicação de terceiros fora da allow-list não deve conseguir ler a resposta pelo navegador.

## Limites e trade-offs
CORS não impede clientes HTTP, scripts de servidor ou aplicativos nativos de chamar a API. Uma requisição simples pode chegar ao servidor mesmo que o navegador depois bloqueie o JavaScript de ler a resposta; portanto, CORS não substitui autorização nem proteção anti-CSRF. Permitir origens demais amplia o conjunto de páginas autorizadas a ler respostas. Respostas em cache exigem cuidado quando a política é dinâmica.

## Como verificar
Teste origens permitidas, não permitidas e `null`; requisições simples e preflight; respostas com e sem credenciais; e o comportamento do cache. Confirme que a API ainda autentica e autoriza chamadas independentemente do cabeçalho CORS e que nenhuma origem arbitrária é refletida.

## Conexões
- [[csrf-token-protecao-web]] — CORS não é defesa CSRF; o servidor ainda precisa validar a intenção das operações autenticadas.
- [[cookies-seguranca-sessao-http]] — o modo de credenciais afeta como cookies podem acompanhar requisições cross-origin.
- [[contrato-openapi-http]] — políticas de origem devem ser documentadas junto à superfície de integração da API.

## Fontes
- [OWASP REST Security Cheat Sheet — CORS](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) — escopo da política e configuração restrita de origens; acesso em 2026-10-01.
- [MDN — Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) — comportamento do navegador, preflight, cabeçalhos e credenciais; acesso em 2026-10-01.
