---
id: software.web.cache-control-diretivas.000001
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [Cache-Control, no-cache, no-store, private, public]
lote: software-cache-http-0006
---

# Diretivas Cache-Control para armazenamento HTTP

## Em uma frase
`Cache-Control` descreve como caches privados e compartilhados podem armazenar, reutilizar e validar respostas HTTP.

## Por que importa
Uma diretiva mal interpretada pode causar cópias desnecessárias, requisições extras ou exposição de uma resposta personalizada por um cache compartilhado. Em particular, `no-cache` não significa “não armazenar”, e `private` não substitui autenticação nem autorização. A política precisa refletir a sensibilidade e a mutabilidade da representação.

## Como funciona
Na resposta, `no-store` proíbe caches de armazenar partes da solicitação ou resposta para reutilização. `no-cache` permite armazenamento, mas exige validação bem-sucedida antes de reutilizar a resposta. `private` impede que um cache compartilhado armazene a resposta sem qualificação, enquanto um cache privado pode armazená-la. `public` indica que qualquer cache pode armazenar a resposta, inclusive em situações em que a regra padrão restringiria cache compartilhado. Essas diretivas não definem por si só quanto tempo uma resposta permanece fresca; diretivas de frescor, como `max-age` e `s-maxage`, tratam da duração.

## Exemplo
Uma página personalizada pode usar `Cache-Control: private, max-age=60` se o navegador puder reutilizá-la por um minuto, mas o proxy compartilhado não. Para dados que não devem ser mantidos por caches conformes, a política pode usar `no-store`. `no-cache` é apropriado quando se permite guardar a cópia, mas o origin precisa confirmar se ela ainda pode ser reutilizada.

## Limites e trade-offs
Uma cache gerenciada por produto pode ter configuração própria, e a RFC observa que suas regras operacionais podem diferir do protocolo HTTP. `no-store` não é mecanismo completo de privacidade contra caches comprometidos, aplicações que guardam dados ou outros sistemas de armazenamento. Diretivas contraditórias devem ser evitadas; não presuma que nomes parecidos tenham o mesmo efeito.

## Como verificar
Inspecione as respostas reais nos headers e teste uma cache privada e uma compartilhada separadamente. Confirme se `no-cache` causa validação, `no-store` evita armazenamento e `private` impede reutilização compartilhada. Teste também a política em respostas com cookies ou autenticação e verifique que cache não substitui autorização da aplicação.

## Conexões
- [[freshness-age-cache-http]] — duração e idade determinam quando uma resposta armazenada fica stale.
- [[cache-respostas-autenticadas-shared]] — políticas de cache compartilhado exigem cuidado com solicitações autenticadas.
- [[stale-while-revalidate-if-error]] — diretivas stale permitem usos específicos após o frescor normal.

## Fontes
- [RFC 9111 — HTTP Caching, seção 5.2.2](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2) — semântica das diretivas de resposta; acesso em 2026-10-01.
- [MDN — Cache-Control header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) — explicação e compatibilidade das diretivas; acesso em 2026-10-01.
