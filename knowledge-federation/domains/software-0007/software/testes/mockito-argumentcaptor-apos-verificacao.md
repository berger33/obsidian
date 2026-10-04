---
id: software.testes.tranche10.000372
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/ArgumentCaptor.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: capturar argumento durante a verificação

## Em uma frase
ArgumentCaptor guarda o argumento passado para uma chamada verificada para permitir assertions específicas sobre seus campos.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Usar um matcher genérico pode não mostrar qual payload foi enviado quando o contrato depende de vários valores relacionados.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Capture durante verify e faça assertions focadas no objeto; prefira ArgumentMatcher se a lógica de comparação for reutilizada em stubbing.

## Exemplo
O teste captura o comando enviado ao broker e valida chave, versão e metadados sem comparar campos não relacionados.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. O Javadoc recomenda captor em verificação, não em stubbing; se a chamada não ocorrer, nenhum argumento será capturado.

## Como verificar
Force ausência da chamada e confirme que a falha aponta a verificação, depois varie um campo relevante do payload.

## Conexões
- [[mockito-stubbing-nao-duplicar-verificacao]] — Veja também: Mockito: não verificar automaticamente uma chamada já stubada.
- [[mockito-matchers-consistencia-em-todos-argumentos]] — Veja também: Mockito: usar matchers em todos os argumentos da chamada.

## Fontes
- [Mockito 5.24.0 — ArgumentCaptor.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/ArgumentCaptor.java) — captura de argumentos e distinção em relação a matchers; consultado em 2026-10-02.
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
