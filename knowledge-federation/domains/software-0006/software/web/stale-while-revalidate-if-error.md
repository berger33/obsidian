---
id: software.web.cache-stale-extensions.000001
tipo: conceito
dominio: software
subdominio: web
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://www.rfc-editor.org/rfc/rfc5861.html", "https://www.rfc-editor.org/rfc/rfc9111.html#section-4.2.4"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [stale-while-revalidate, stale-if-error, Serve stale HTTP cache]
lote: software-cache-http-0006
---

# stale-while-revalidate e stale-if-error

## Em uma frase
Extensões `stale-while-revalidate` e `stale-if-error` permitem que uma cache use uma resposta stale em janelas limitadas para reduzir latência ou tolerar falhas do origin.

## Por que importa
Depois do frescor normal, uma cache pode precisar validar com o origin, o que acrescenta latência e depende da disponibilidade do serviço. Em certos conteúdos, a equipe aceita servir por pouco tempo uma versão potencialmente desatualizada para manter disponibilidade ou fazer validação em segundo plano. Essa decisão deve ser explícita porque há um compromisso entre frescor e disponibilidade.

## Como funciona
A RFC 5861, documento informativo, define `stale-while-revalidate=N`: a cache pode servir a resposta depois de ela ficar stale por até N segundos e deve tentar revalidá-la sem bloquear quando a extensão motivar o uso stale. `stale-if-error=N` permite que uma cópia stale seja usada se ocorrer erro, incluindo respostas 500, 502, 503 ou 504, respeitando o limite de staleness. Os limites são adicionais à vida de frescor normal; depois da janela, a extensão deixa de autorizar o uso. A RFC 9111 descreve ainda o tratamento geral de respostas stale e as restrições de diretivas como `no-cache` e `must-revalidate`.

## Exemplo
`Cache-Control: max-age=600, stale-while-revalidate=30` declara 600 segundos de frescor e permite uma janela adicional de até 30 segundos em que a cache pode responder enquanto revalida. Um catálogo público de baixa criticidade pode tolerar essa janela; saldo ou autorização sensível normalmente não deve usar stale sem uma análise explícita de risco.

## Limites e trade-offs
A extensão é permissiva: `MAY` não obriga todas as caches a servir conteúdo stale. A janela pode expor mudanças recentes por mais tempo e ausência de tráfego não garante revalidação em segundo plano. Diretivas mais restritivas podem proibir servir stale. A RFC 5861 é informativa e suporte/comportamento de browser, proxy ou CDN precisa ser verificado no produto real.

## Como verificar
Em uma cache de teste, reduza o TTL, mantenha o origin acessível durante `stale-while-revalidate` e depois simule uma falha coberta por `stale-if-error`. Observe se a versão stale é servida, qual `Age` aparece e quando a janela termina. Teste também `no-cache`/`must-revalidate` e confirme que a política da cache respeita restrições aplicáveis.

## Conexões
- [[freshness-age-cache-http]] — as janelas stale começam depois da vida normal de frescor.
- [[cache-control-diretivas-armazenamento-http]] — diretivas de armazenamento e revalidação podem restringir o uso stale.
- [[cache-respostas-autenticadas-shared]] — não aplicar tolerância stale a conteúdo privado sem avaliar exposição e consistência.

## Fontes
- [RFC 5861 — HTTP Cache-Control Extensions for Stale Content](https://www.rfc-editor.org/rfc/rfc5861.html) — extensões e seus limites temporais; acesso em 2026-10-01.
- [RFC 9111 — HTTP Caching, seção 4.2.4](https://www.rfc-editor.org/rfc/rfc9111.html#section-4.2.4) — regras gerais para servir respostas stale; acesso em 2026-10-01.
