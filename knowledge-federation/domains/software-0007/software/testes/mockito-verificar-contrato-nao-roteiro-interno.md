---
id: software.testes.tranche10.000370
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: verificar contrato observável do colaborador

## Em uma frase
verify verifica se uma interação esperada ocorreu e pode limitar a quantidade de chamadas.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Verificar cada detalhe interno da implementação faz refatorações sem mudança de comportamento quebrarem testes úteis.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Priorize o resultado observável e verifique chamadas apenas quando o efeito do colaborador fizer parte do contrato relevante.

## Exemplo
Um teste confirma que o gateway enviou uma cobrança uma vez e também valida o status retornado ao serviço chamador.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. verifyNoMoreInteractions pode tornar o teste excessivamente prescritivo se usado como regra automática para todos os mocks.

## Como verificar
Altere a ordem interna sem alterar o efeito esperado e confirme que o teste falha somente quando o contrato deixa de ser respeitado.

## Conexões
- [[mockito-stubbing-nao-duplicar-verificacao]] — Veja também: Mockito: não verificar automaticamente uma chamada já stubada.

## Fontes
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
- [Mockito 5.24.0 — Strictness.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java) — níveis de strictness e benefícios/limitações de STRICT_STUBS; consultado em 2026-10-02.
