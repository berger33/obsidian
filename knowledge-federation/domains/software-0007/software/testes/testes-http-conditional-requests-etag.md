---
id: software.testes.tranche07.000143
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://www.rfc-editor.org/rfc/rfc9110.html", "https://www.rfc-editor.org/rfc/rfc6585.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Testes de requisições condicionais e ETag", "Teste: Testes de requisições condicionais e ETag"]
lote: software-testes-2000-0001
---

# Testes de requisições condicionais e ETag

## Em uma frase
Exercite validators e precondições HTTP para detectar cache condicional e conflitos de atualização sem sobrescrever silenciosamente estado concorrente.

## Por que importa
Duas escritas concorrentes podem perder atualização; validators permitem que o cliente condicione ação à representação que observou.

## Como funciona
Obtenha ETag, faça GET condicional com If-None-Match e verifique resposta de revalidação prevista; depois envie If-Match válido e desatualizado para operação de escrita. Compare 412 e eventual uso de 428 conforme contrato.

## Exemplo
Dois clientes leem a mesma versão; A atualiza com If-Match, B tenta atualizar com o ETag antigo e recebe precondition failure, sem apagar a alteração de A.

## Limites e trade-offs
ETag pode ser forte ou fraco e comparação depende do cabeçalho/método; não invente algoritmo de ETag. 428 é opcional e caches têm regras próprias.

## Como verificar
Registre validator, status e estado final em concorrência controlada; valide corpo e cabeçalhos para correspondência atual e obsoleta e confirme que revalidação GET não retorna conteúdo indevido.

## Conexões
- [[concorrencia-otimista-etag-if-match]] — aprofundamento relacionado.
- [[revalidacao-cache-etag-if-none-match]] — aprofundamento relacionado.

## Fontes
- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica de métodos, representação, negociação e precondições HTTP; consultado em 2026-10-01.
- [IETF RFC 6585 — Additional HTTP Status Codes](https://www.rfc-editor.org/rfc/rfc6585.html) — 429 Too Many Requests e 428 Precondition Required; consultado em 2026-10-01.
