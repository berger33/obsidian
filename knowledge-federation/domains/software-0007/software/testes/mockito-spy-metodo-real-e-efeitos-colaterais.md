---
id: software.testes.tranche10.000376
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: considerar execução real ao configurar um spy

## Em uma frase
Um spy delega chamadas não stubadas ao objeto real, diferentemente do mock que usa comportamento simulado.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. A expressão when(spy.method()) pode chamar o método real durante a configuração e causar efeito colateral antes do exercício principal.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Use doReturn/doThrow quando a configuração de um spy não deve executar o método real e prefira mock quando não precisa do comportamento real.

## Exemplo
Um spy sobre cache evita executar a operação de I/O no setup por meio de doReturn, mas deixa outros métodos reais deliberadamente ativos.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. Spies continuam dependentes de detalhes e estado real do objeto; configuração parcial pode ser difícil de entender.

## Como verificar
Conte chamadas reais durante a configuração e confirme que nenhuma rede, gravação ou mutação ocorre antes da fase de ação do teste.

## Conexões
- [[mockito-lenient-apenas-no-stub-excepcional]] — Veja também: Mockito: limitar lenient a stubs realmente excepcionais.
- [[mockito-stubbing-consecutivo-modelar-retentativas]] — Veja também: Mockito: usar stubbing consecutivo para sequência legítima.

## Fontes
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
- [Mockito JUnit Jupiter 5.24.0 — MockitoExtension.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java) — integração do Mockito com o ciclo de testes JUnit Jupiter; consultado em 2026-10-02.
