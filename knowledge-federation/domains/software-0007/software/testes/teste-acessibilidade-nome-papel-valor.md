---
id: software.testes.tranche07.000113
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://www.w3.org/TR/wai-aria-1.2/", "https://www.w3.org/WAI/ARIA/apg/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de nome, papel e estado de controles", "Teste: Teste de nome, papel e estado de controles"]
lote: software-testes-2000-0001
---

# Teste de nome, papel e estado de controles

## Em uma frase
Valide se controles nativos e customizados expõem nome acessível, papel e estado coerentes com a função e com a interação atual.

## Por que importa
Tecnologias assistivas dependem da semântica exposta pela interface; um controle visualmente parecido pode ser inutilizável se seu nome ou estado não for anunciado corretamente.

## Como funciona
Inspecione a árvore de acessibilidade e compare nome, role, valor ou estado com o rótulo visível e a função. Para widgets ARIA, verifique interação de teclado do padrão correspondente e se estados como expandido, selecionado ou marcado são atualizados.

## Exemplo
Ao acionar um botão de expansão, confirme que leitor de tela anuncia o nome, papel de botão e estado expandido; ao recolher, o estado retorna e o conteúdo deixa de ser apresentado como aberto.

## Limites e trade-offs
WAI-ARIA não substitui controles HTML nativos quando estes atendem à necessidade. Combinar atributos conflitantes ou testar apenas a árvore sem operação real pode ocultar falhas de teclado e comportamento.

## Como verificar
Execute sequência de teclado, compare árvore antes/depois e teste o comportamento em combinações de browser e tecnologia assistiva compatíveis com o produto.

## Conexões
- [[teste-acessibilidade-navegacao-teclado]] — aprofundamento relacionado.
- [[teste-acessibilidade-status-dinamico]] — aprofundamento relacionado.

## Fontes
- [W3C — WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) — semântica de papéis, estados e propriedades acessíveis; consultado em 2026-10-01.
- [W3C WAI — ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — padrões de teclado e semântica para widgets ARIA; consultado em 2026-10-01.
