---
id: software.testes.tranche10.000378
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

# Mockito: preferir mocks novos a resetar estado compartilhado

## Em uma frase
reset apaga stubbing e interações de um mock, enquanto clearInvocations limpa interações sem remover o comportamento configurado.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Mocks compartilhados entre testes podem transportar estado e fazer o resultado depender da ordem ou de uma limpeza esquecida.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Crie os mocks no escopo de cada teste; use reset ou clearInvocations apenas quando uma fase do mesmo teste justificar explicitamente.

## Exemplo
Cada método cria um novo mock de repositório; duas fases de um teste usam clearInvocations quando precisam separar somente as chamadas observadas.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. Limpar interações não equivale a recriar uma dependência, e reset não deve esconder uma fixture que deveria ser local.

## Como verificar
Execute testes em ordem inversa e em paralelo para detectar estado que atravessa a fronteira entre casos.

## Conexões
- [[mockito-stubbing-consecutivo-modelar-retentativas]] — Veja também: Mockito: usar stubbing consecutivo para sequência legítima.
- [[mockito-junit-jupiter-lifecycle-explicito]] — Veja também: Mockito: registrar a extensão JUnit Jupiter para inicializar mocks.

## Fontes
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
- [Mockito JUnit Jupiter 5.24.0 — MockitoExtension.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java) — integração do Mockito com o ciclo de testes JUnit Jupiter; consultado em 2026-10-02.
