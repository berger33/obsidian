---
id: software.testes.tranche10.000402
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://java.testcontainers.org/test_framework_integration/junit_5/", "https://java.testcontainers.org/test_framework_integration/manual_lifecycle_control/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testcontainers JUnit: escolher container compartilhado ou por teste

## Em uma frase
A extensão Jupiter associa containers estáticos ao ciclo de vida da classe e containers de instância ao lifecycle por teste.

## Por que importa
Testcontainers aproxima testes de integração de serviços reais, mas containers iniciados não significam necessariamente que o serviço já esteja pronto. Compartilhar serviço reduz inicializações, mas torna persistência de dados e concorrência parte explícita do desenho.

## Como funciona
Declare imagem e lifecycle, aguarde um sinal de readiness adequado ao protocolo e isole recursos mutáveis entre casos e workers. Use container por teste quando isolamento importar; use static compartilhado quando os dados forem controlados e limpeza for confiável.

## Exemplo
Vários métodos usam o mesmo broker em static container, cada um com tópico exclusivo e limpeza depois da assertion.

## Limites e trade-offs
Integração com Docker, custo de recursos, versão de imagem e comportamento do framework influenciam a reprodutibilidade e a duração da suíte. O lifecycle do container não limpa automaticamente todos os registros, tópicos ou objetos criados pelo teste.

## Como verificar
Rode métodos em ordem aleatória e confirme que cada caso cria e remove seu próprio dado mutável.

## Conexões
- [[testcontainers-wait-endpoint-readiness-contract]] — Veja também: Testcontainers: escolher wait strategy alinhada ao protocolo.
- [[testcontainers-junit5-parallel-extension-limit]] — Veja também: Testcontainers JUnit: não presumir paralelismo seguro da extensão.

## Fontes
- [Testcontainers for Java — JUnit 5 integration](https://java.testcontainers.org/test_framework_integration/junit_5/) — containers estáticos/de instância e limitações de paralelismo da extensão; consultado em 2026-10-02.
- [Testcontainers for Java — Manual lifecycle control](https://java.testcontainers.org/test_framework_integration/manual_lifecycle_control/) — controle explícito de start/stop e compartilhamento do ciclo de vida; consultado em 2026-10-02.
