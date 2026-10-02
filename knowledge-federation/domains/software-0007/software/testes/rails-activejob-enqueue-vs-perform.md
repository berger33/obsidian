---
id: software.testes.tranche14.000807
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://api.rubyonrails.org/classes/ActiveJob/TestHelper.html", "https://guides.rubyonrails.org/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rails: distinguir job enfileirado de job executado

## Em uma frase
Active Job oferece helpers de teste para observar jobs enfileirados e executar jobs sob demanda com o adapter de teste.

## Por que importa
Uma assertion de enqueue cobre intenção de delegar trabalho, enquanto uma assertion de execução cobre comportamento do `perform`; são contratos diferentes.

## Como funciona
Use `perform_later` e assertions de fila para verificar agendamento, ou `perform_now`/helper de perform para testar o corpo com entradas controladas.

## Exemplo
Um teste de controller confirma que uma rotina de relatório foi enfileirada; um teste separado confirma que o job gera o resultado para os dados fornecidos.

## Limites e trade-offs
Adapter de teste não valida latência, retry e disponibilidade do backend de produção.

## Como verificar
Examine fila, argumentos e número de execuções, e mantenha teste de integração do backend apenas onde o risco exigir.

## Conexões
- [[rails-freeze-time-helper-cleanup]] — Veja também: Rails: congelar o relógio com restauração garantida.
- [[rails-mailer-generation-and-delivery-tests]] — Veja também: Rails: separar conteúdo de mailer da entrega.

## Fontes
- [Rails 8.1 — ActiveJob::TestHelper](https://api.rubyonrails.org/classes/ActiveJob/TestHelper.html) — assertions para jobs enfileirados e executados, argumentos e filas; consultado em 2026-10-02.
- [Rails 8.1 — Testing Rails Applications](https://guides.rubyonrails.org/testing.html) — ambiente, fixtures, testes funcionais, integração, system tests e paralelismo; consultado em 2026-10-02.
