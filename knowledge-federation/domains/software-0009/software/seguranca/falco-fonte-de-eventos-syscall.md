---
id: software.seguranca.tranche17.001661
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://falco.org/docs/concepts/event-sources/", "https://falco.org/docs/reference/rules/default-rules/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Falco: Fonte de eventos syscall

## Em uma frase
**Falco — Fonte de eventos syscall:** Falco avalia eventos de chamadas de sistema do kernel por uma fonte que é habilitada por padrão.

## Por que importa
O recorte de **fonte de eventos syscall** ajuda a identificar comportamentos de risco no host ou container e encaminhar alertas acionáveis para resposta. A equipe registra risco, evidência e responsável.

## Como funciona
Para **fonte de eventos syscall**, uma fonte de eventos emite dados; regras correlacionadas àquela fonte avaliam condições e produzem alertas com prioridade e contexto. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em host de teste, gere execução de processo fora do caminho esperado e examine evento sem expor workloads reais. Teste em staging autorizado.

## Limites e trade-offs
Coleta de syscall requer driver e permissões compatíveis com o kernel e a implantação escolhida. Exceções exigem responsável e prazo.

## Como verificar
Confirme driver ativo, evento de teste e identidade do processo exibida no alerta. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[falco-fontes-de-eventos-via-plugins]] — Complementa o tópico com falco: fontes de eventos via plugins.

## Fontes
- [Falco — Event Sources](https://falco.org/docs/concepts/event-sources/) — documentação oficial sobre origens de eventos e avaliação por fonte; consultado em 2026-10-04.
- [Falco — Default Rules](https://falco.org/docs/reference/rules/default-rules/) — catálogo oficial de regras padrão, maturidade, condições e prioridades; consultado em 2026-10-04.
