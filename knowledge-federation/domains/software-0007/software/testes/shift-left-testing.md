---
id: software.testes.shift-left.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Shift left in testing", "Shift left antecipa testes sem eliminar verificações tardias"]
lote: software-testes-2000-0001
---

# Shift left antecipa testes sem eliminar verificações tardias

## Em uma frase
Shift left significa iniciar atividades de teste mais cedo no SDLC, e não abandonar os testes necessários nas etapas posteriores.

## Por que importa
Defeitos encontrados em requisitos, desenho e código antes da integração tendem a ser mais baratos de investigar e corrigir. Porém, algumas propriedades só podem ser avaliadas adequadamente com sistema integrado e ambiente representativo.

## Como funciona
O CTFL liga shift left ao princípio de teste antecipado: revisar especificações, escrever casos antes do código, executar análise estática e, quando possível, começar testes não funcionais em níveis inferiores. A mesma orientação ressalta que testar cedo não significa negligenciar o trabalho mais adiante no SDLC.

## Exemplo
Testers revisam critérios de autenticação enquanto a história é refinada e preparam casos de componente durante a implementação. Depois que o serviço se integra ao provedor de identidade, a equipe testa comportamento da interface real e recuperação de falhas.

## Limites e trade-offs
Antecipar não substitui o nível apropriado: uma revisão de contrato não mede latência de produção; um teste de componente não prova integração externa. Shift left exige participação e capacidade no momento certo.

## Como verificar
Cheque se revisão e análise começam junto aos rascunhos, e se permanecem testes de sistema, integração e aceitação necessários ao risco.

## Conexões
- [[static-testing-work-products]] — revisões antecipadas avaliam artefatos sem executá-los.
- [[test-levels-overview]] — níveis diferentes preservam objetivos posteriores.

## Fontes
- [ASTQB — CTFL §2.1.5, Shift Left](https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/) — significado e exemplos; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.1.5; acesso em 2026-10-01.
