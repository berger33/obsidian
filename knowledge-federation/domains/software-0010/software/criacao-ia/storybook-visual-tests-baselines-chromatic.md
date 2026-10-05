---
id: software.criacao_ia.tranche05.000468
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://storybook.js.org/docs/writing-tests/visual-testing", "https://www.chromatic.com/docs/visual-tests/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: detectar regressões de pixels com visual tests e baselines revisados

## Em uma frase
Testes visuais comparam snapshots renderizados de histórias contra baselines e destacam diferenças de pixels para revisão.

## Por que importa
Mudanças de CSS, tipografia ou layout podem quebrar a aparência sem alterar texto ou comportamento funcional que um teste unitário verifica.

## Como funciona
Configure o addon oficial de visual testing conectado ao Chromatic, crie baseline inicial e execute a comparação após mudanças; aceite atualizações somente quando o diff for intencional.

## Exemplo
Uma alteração na largura do botão gera diff para stories afetadas; o revisor compara pixels no painel, corrige regressão ou aprova baseline de mudança deliberada.

## Limites e trade-offs
O fluxo descrito envia stories ao serviço cloud Chromatic; screenshots não provam acessibilidade, lógica interna ou correção em toda combinação de dispositivo.

## Como verificar
Faça uma mudança cosmética controlada, confirme que o diff é detectado, depois restaure ou aceite baseline e valide repetibilidade no CI.

## Conexões
- [[storybook-vitest-addon-stories-como-component-tests]] — Storybook: executar stories como component tests com addon Vitest.
- [[storybook-autodocs-tags-living-documentation]] — Storybook: habilitar Autodocs por tag e estender a documentação com MDX.

## Fontes
- [Storybook — Visual tests](https://storybook.js.org/docs/writing-tests/visual-testing) — Descreve snapshots, baselines, comparação de pixels e integração Chromatic. Consulta: 2026-10-04.
- [Chromatic visual testing](https://www.chromatic.com/docs/visual-tests/) — Especifica revisão de mudanças visuais e configuração de testes visuais hospedados. Consulta: 2026-10-04.
