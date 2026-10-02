---
id: software.seguranca.oauth-pkce.000001
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://www.rfc-editor.org/rfc/rfc9700.html", "https://www.rfc-editor.org/rfc/rfc7636.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
aliases: [PKCE, Proof Key for Code Exchange, OAuth Authorization Code]
lote: software-seguranca-0003
---

# PKCE no fluxo Authorization Code do OAuth

## Em uma frase
PKCE vincula a troca de um código de autorização OAuth a um segredo temporário que o cliente criou para aquela transação.

## Por que importa
Aplicativos nativos e outros clientes públicos não conseguem guardar com segurança um segredo compartilhado embutido no aplicativo. Além disso, um código de autorização pode ser interceptado no caminho de retorno ao cliente. Com PKCE, conhecer apenas o código não basta para resgatá-lo: o cliente também precisa provar que possui o verificador associado à solicitação original.

## Como funciona
O cliente gera um `code_verifier` imprevisível e específico para cada tentativa. Antes de redirecionar o usuário, calcula um `code_challenge` e o envia junto à solicitação de autorização. No método `S256`, o desafio é o SHA-256 do verificador, codificado em Base64 URL-safe sem padding. O servidor associa o desafio ao código emitido. Na troca do código por tokens, o cliente envia o verificador original; o servidor calcula novamente o desafio e compara os valores. A RFC 7636 define o formato e o tamanho do verificador. A RFC 9700 exige PKCE para clientes públicos, recomenda seu uso para clientes confidenciais e aponta `S256` como o método que não expõe o verificador na solicitação.

## Exemplo
Um aplicativo móvel inicia um login e cria um verificador novo para essa transação. Ele envia somente o desafio `S256` ao servidor de autorização. Ao receber o código de retorno, envia o código e o verificador ao endpoint de tokens. Um código capturado por outro aplicativo não pode ser trocado sem o verificador correto.

## Limites e trade-offs
PKCE não transforma um aplicativo público em cliente confidencial e não substitui TLS, validação exata de URI de redirecionamento, proteção dos tokens ou controles do fluxo OAuth. Não reutilize desafios/verificadores entre transações nem trate o `code_challenge` como segredo. Bibliotecas conhecidas reduzem erros de codificação e de validação; parâmetros como `state` continuam importantes quando necessários para correlacionar estado local e resposta.

## Como verificar
Confirme que cada fluxo gera um verificador novo, que o desafio usa `S256`, que o endpoint rejeita um verificador ausente ou incorreto e que um código não pode ser resgatado duas vezes. Teste também o redirecionamento e a vinculação do desafio ao código no servidor de autorização.

## Conexões
- [[csrf-token-protecao-web]] — ambos protegem fluxos de navegador contra requisições não vinculadas à intenção legítima, mas não são controles intercambiáveis.
- [[cookies-seguranca-sessao-http]] — a sessão autenticada exige proteção própria depois do fluxo OAuth.
- [[contrato-openapi-http]] — a especificação da API deve refletir os requisitos reais do endpoint de autorização e de tokens.

## Fontes
- [RFC 9700 — Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html) — recomendações atuais, incluindo o uso de PKCE; acesso em 2026-10-01.
- [RFC 7636 — Proof Key for Code Exchange by OAuth Public Clients](https://www.rfc-editor.org/rfc/rfc7636.html) — criação e verificação de `code_verifier` e `code_challenge`; acesso em 2026-10-01.
