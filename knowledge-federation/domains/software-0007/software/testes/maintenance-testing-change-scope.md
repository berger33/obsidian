---
id: software.testes.maintenance-scope.000001
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
fontes: ["https://astqb.org/2-3-maintenance-testing/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Maintenance testing scope", "Manutenção de software: dimensionar o teste pela mudança"]
lote: software-testes-2000-0001
---

# Manutenção de software: dimensionar o teste pela mudança

## Em uma frase
O escopo de teste de manutenção costuma depender do risco da mudança, do tamanho do sistema existente e do tamanho da alteração.

## Por que importa
Uma correção localizada pode afetar comportamento distante por acoplamento, configuração compartilhada ou dados persistentes. Repetir sempre a suíte inteira pode ser inviável, mas testar apenas a linha alterada também pode deixar regressões relevantes sem observação.

## Como funciona
O CTFL caracteriza teste de manutenção como avaliação de alterações em sistema operacional, incluindo sucesso da implementação e busca de regressões em partes não alteradas. O alcance é decidido com análise de impacto e risco, considerando dimensão da mudança e do produto. Testes de confirmação verificam a mudança; a seleção de regressão considera o que pode ter sido afetado.

## Exemplo
Uma atualização de regra tributária pode exigir casos específicos da correção, caminhos que compartilham o cálculo e reconciliação de relatórios. Uma troca de ícone de baixo risco não implica automaticamente repetir todos os testes de desempenho, desde que o impacto esteja justificado.

## Limites e trade-offs
Análise de impacto depende de rastreabilidade e conhecimento do sistema; estimativas podem falhar em arquitetura pouco documentada. “Mudança pequena” não é prova de risco pequeno.

## Como verificar
Registre mudança, dependências, riscos e conjuntos de testes selecionados; justifique exclusões e verifique efeitos após implantação.

## Conexões
- [[regression-test-prioritization-risco-impacto]] — prioriza regressão conforme risco e impacto.
- [[test-environment-configuration-management]] — identifica versão de sistema e configuração.

## Fontes
- [ASTQB — CTFL §2.3, Maintenance Testing](https://astqb.org/2-3-maintenance-testing/) — fatores de escopo e regressão em manutenção; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.3; acesso em 2026-10-01.
