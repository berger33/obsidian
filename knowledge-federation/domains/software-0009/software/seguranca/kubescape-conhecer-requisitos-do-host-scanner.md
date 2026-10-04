---
id: software.seguranca.tranche18.001739
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://kubescape.io/docs/scanning/", "https://kubescape.io/docs/frameworks-and-controls/frameworks/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Kubescape: Conhecer requisitos do host scanner

## Em uma frase
**Kubescape — Conhecer requisitos do host scanner:** Alguns controles dependem de observações nos nós e podem exigir o operador e agentes correspondentes.

## Por que importa
O recorte de **conhecer requisitos do host scanner** ajuda a encontrar desvios de configuração antes e depois da implantação com resultados ligados a recursos e controles. A equipe registra risco, evidência e responsável.

## Como funciona
Para **conhecer requisitos do host scanner**, o operador escolhe origem, framework ou control, executa o scan e revisa evidências antes de aplicar remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Planeje um scan de laboratório para controles de kubelet com acesso de host devidamente revisado. Teste em staging autorizado.

## Limites e trade-offs
Scan de API sozinho não oferece evidência para controles dependentes do nó. Exceções exigem responsável e prazo.

## Como verificar
Confira na saída e na documentação quais controles foram ignorados por ausência do host scanner. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubescape-publicar-resultados-junit-em-ci]] — Complementa o tópico com kubescape: publicar resultados junit em ci.

## Fontes
- [Kubescape — Scanning](https://kubescape.io/docs/scanning/) — documentação oficial de scans de cluster, arquivos, controls, score e exceções; consultado em 2026-10-04.
- [Kubescape — Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/) — catálogo oficial de frameworks e controles de segurança; consultado em 2026-10-04.
