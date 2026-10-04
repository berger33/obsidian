---
id: software.seguranca.csrf-tokens.000001
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html", "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
aliases: [CSRF, Cross-Site Request Forgery, token anti-CSRF]
lote: software-seguranca-0003
---

# Tokens anti-CSRF em aplicações web

## Em uma frase
Uma defesa anti-CSRF exige que cada operação autenticada que altera estado prove que a requisição foi iniciada por um fluxo legítimo da aplicação, e não apenas acompanhada de um cookie válido.

## Por que importa
Navegadores enviam cookies de sessão automaticamente em diversas requisições. Um site externo pode tentar induzir o navegador de uma pessoa autenticada a submeter uma ação ao serviço legítimo. O navegador pode anexar a sessão sem que a aplicação consiga inferir, apenas pelo cookie, que a pessoa pretendia aquela mudança.

## Como funciona
Em aplicações com estado no servidor, o padrão synchronizer token gera um valor imprevisível ligado à sessão e exige que o cliente o envie em operações que alteram estado; o servidor compara o valor antes de executar a ação. Aplicações sem sessão podem usar um padrão double-submit, mas a OWASP recomenda uma variante assinada com HMAC em vez de confiar em dois valores copiáveis. Frameworks com proteção CSRF integrada devem ser avaliados antes de criar um mecanismo próprio. `SameSite` em cookies, validação de `Origin` e Fetch Metadata podem reforçar a defesa, mas sua adequação depende do modelo de cliente.

## Exemplo
Um formulário de alteração de e-mail recebe um token associado à sessão. No envio, o servidor valida o token e a permissão antes de gravar a mudança. Uma requisição que contenha apenas o cookie de sessão, sem token válido, é recusada e não altera os dados. A mesma regra cobre chamadas assíncronas que mudam estado.

## Limites e trade-offs
Não use `GET` para alterar estado: navegações e pré-carregamentos podem dispará-lo, e algumas políticas `SameSite` ainda permitem navegações seguras. Tokens por requisição podem reduzir a janela de reutilização, mas invalidar formulários abertos e causar problemas com o botão “voltar”; a decisão precisa ser testada. XSS pode permitir que código malicioso execute ações na origem legítima e contorne várias defesas CSRF. CORS, sozinho, não impede que uma requisição cross-site chegue ao servidor.

## Como verificar
Catalogue endpoints que alteram estado e teste cada um sem token, com token ausente, incorreto, expirado e válido. Confirme que a falha não modifica estado. Verifique também que métodos seguros não realizam mutações e que a configuração funciona nos fluxos legítimos de login, formulários e chamadas assíncronas.

## Conexões
- [[cookies-seguranca-sessao-http]] — explica por que cookies de autenticação são enviados automaticamente e quais atributos ajudam como defesa adicional.
- [[cors-origem-nao-autorizacao]] — CORS controla leitura de respostas pelo navegador, não substitui a validação anti-CSRF no servidor.
- [[oauth-pkce-fluxo-codigo]] — PKCE vincula um código OAuth à transação, com escopo diferente de um token CSRF de sessão.

## Fontes
- [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) — padrões de token e defesas em profundidade; acesso em 2026-10-01.
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) — comportamento de cookies de sessão e relação com CSRF; acesso em 2026-10-01.
