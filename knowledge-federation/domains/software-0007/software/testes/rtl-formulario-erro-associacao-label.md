---
id: software.testes.tranche08.000164
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://testing-library.com/docs/queries/about/", "https://testing-library.com/docs/user-event/intro/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testing Library: validar formulários pela relação label-controle

## Em uma frase
Teste que campos de formulário tenham nome acessível e que mensagens de validação sejam associadas ao controle correto.

## Por que importa
Encontrar input por placeholder pode ignorar a ausência de label e deixar uma barreira de uso passar despercebida.

## Como funciona
Localize o campo por label ou role e nome, interaja com user-event e verifique erro visível e atributos relacionais quando o requisito os envolve.

## Exemplo
Submeta e-mail vazio, localize o textbox pelo nome E-mail e verifique mensagem de obrigatoriedade anunciada e vinculada à entrada.

## Limites e trade-offs
Uma assertion DOM não substitui teste manual ou automatizado com leitor de tela em fluxos complexos; valide comportamento compatível com requisitos reais.

## Como verificar
Remova temporariamente o label ou associação do erro e confirme que o teste detecta a regressão. Verifique estado válido e inválido sem depender de classe CSS.

## Conexões
- [[rtl-consultas-prioridade-role-name]] — Veja também: Testing Library: priorizar consultas por papel e nome.
- [[rtl-fetch-loading-empty-error-states]] — Veja também: Testing Library: cobrir loading, vazio e erro de carregamento.

## Fontes
- [Testing Library — About Queries](https://testing-library.com/docs/queries/about/) — seleção de elementos por papel, nome e prioridade; consultado em 2026-10-02.
- [Testing Library — user-event](https://testing-library.com/docs/user-event/intro/) — simulação de interações de usuário acima de eventos DOM isolados; consultado em 2026-10-02.
