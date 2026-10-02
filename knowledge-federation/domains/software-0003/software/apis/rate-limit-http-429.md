---
id: software.apis.rate-limit-http.000001
tipo: tecnica
dominio: software
subdominio: apis
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://www.rfc-editor.org/rfc/rfc6585.html#section-4", "https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3"]
tags: [dominio/software, subdominio/apis, qualidade/candidata]
aliases: [HTTP 429, Too Many Requests, rate limiting]
lote: software-seguranca-0003
---

# Limitação de taxa e HTTP 429

## Em uma frase
Um limite de taxa protege capacidade e uso justo de uma API; `429 Too Many Requests` informa que o servidor recusou uma requisição por excesso de solicitações dentro de uma política definida pelo serviço.

## Por que importa
Sem limites, um cliente com defeito, abuso automatizado ou pico inesperado pode consumir recursos compartilhados e prejudicar outras pessoas. Uma resposta previsível também permite que clientes cooperativos reduzam o ritmo em vez de repetir imediatamente a mesma operação. A política é parte do contrato operacional da API e precisa considerar custo, risco e comportamento legítimo do produto.

## Como funciona
RFC 6585 define o status `429` e permite que a resposta inclua `Retry-After`. RFC 9110 define esse campo como uma data HTTP ou um número de segundos que indica quanto esperar antes de uma nova tentativa. O padrão não determina qual algoritmo de limitação usar, qual identidade limitar ou quais campos adicionais de quota uma API deve expor. Um serviço pode aplicar políticas distintas por conta, token, rota ou outra chave, desde que documente o escopo. O cliente deve respeitar `Retry-After` quando presente e combinar a espera com limites locais e jitter para evitar um pico sincronizado.

## Exemplo
Uma API recebe mais chamadas de busca do que a política permite para aquele token e responde `429`. Se souber quando a janela de bloqueio termina, pode enviar `Retry-After` em segundos. O cliente interrompe novas tentativas até o momento indicado, aplica jitter e não repete uma operação mutável sem garantia de idempotência.

## Limites e trade-offs
Um limite global simples pode punir usuários legítimos atrás do mesmo NAT ou falhar quando a aplicação opera em várias instâncias. Cabeçalhos de quota específicos podem ter semântica própria e não devem ser tratados como padrão universal sem um contrato. Respostas `429` não corrigem abuso distribuído por si só; exigem métricas, alertas e decisões de escalonamento. Evite confiar em identificadores de IP fornecidos diretamente pelo cliente quando há proxies intermediários.

## Como verificar
Teste o comportamento no limite, imediatamente acima dele e após a recuperação. Confirme escopo consistente entre instâncias, inclusão e interpretação de `Retry-After`, ausência de retries agressivos e impacto sobre clientes legítimos. Meça rejeições, latência, custo e tentativas repetidas para ajustar a política sem ocultar indisponibilidade.

## Conexões
- [[problem-details-rfc9457]] — Problem Details pode explicar de forma estruturada uma resposta 429.
- [[timeouts-retries-backoff-jitter]] — o cliente deve limitar retries e evitar amplificar a sobrecarga.
- [[idempotencia-http-api]] — repetir uma mutação exige considerar seus efeitos e a semântica idempotente.

## Fontes
- [RFC 6585, seção 4 — 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4) — definição do status e uso opcional de `Retry-After`; acesso em 2026-10-01.
- [RFC 9110, seção 10.2.3 — Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3) — sintaxe e semântica do tempo de espera; acesso em 2026-10-01.
