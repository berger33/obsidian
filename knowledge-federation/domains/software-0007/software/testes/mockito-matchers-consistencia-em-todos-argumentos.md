---
id: software.testes.tranche10.000373
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/ArgumentCaptor.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: usar matchers em todos os argumentos da chamada

## Em uma frase
Quando um argumento de uma invocação usa matcher, todos os argumentos dessa mesma invocação precisam ser representados por matchers.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Misturar valor literal com any ou eq pode disparar erro de uso inválido e mascarar a intenção do stub.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Envolva valores fixos em eq e use matchers compatíveis para cada posição da chamada.

## Exemplo
Um stub de enviar(id, payload) usa eq("pedido-7") para o id e any(Payload.class) para o objeto.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. any e eq registram matchers para a próxima operação e não funcionam como valores comuns fora desse contexto.

## Como verificar
Adicione uma chamada com um argumento literal misturado e confirme que o teste reproduz o erro antes de corrigir todos os argumentos.

## Conexões
- [[mockito-argumentcaptor-apos-verificacao]] — Veja também: Mockito: capturar argumento durante a verificação.
- [[mockito-strict-stubs-detectar-setup-morto]] — Veja também: Mockito: usar STRICT_STUBS para expor stubs desnecessários.

## Fontes
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
- [Mockito 5.24.0 — ArgumentCaptor.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/ArgumentCaptor.java) — captura de argumentos e distinção em relação a matchers; consultado em 2026-10-02.
