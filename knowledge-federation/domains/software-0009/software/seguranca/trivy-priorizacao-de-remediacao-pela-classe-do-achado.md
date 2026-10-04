---
id: software.seguranca.tranche17.001610
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
fontes: ["https://trivy.dev/latest/docs/target/container_image/", "https://trivy.dev/latest/docs/scanner/misconfiguration/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Trivy: Priorização de remediação pela classe do achado

## Em uma frase
**Trivy — Priorização de remediação pela classe do achado:** Pacotes vulneráveis, configuração insegura, segredo e licença representam riscos diferentes e pedem responsáveis e correções diferentes.

## Por que importa
O recorte de **priorização de remediação pela classe do achado** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **priorização de remediação pela classe do achado**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Classifique findings de uma imagem de demonstração por tipo e encaminhe pacote ao time de dependências e IaC ao time de plataforma. Teste em staging autorizado.

## Limites e trade-offs
Uma severidade agregada não captura exposição, alcançabilidade ou compensações do ambiente; decisão requer contexto. Exceções exigem responsável e prazo.

## Como verificar
Audite uma amostra contra a política de triagem e confirme que tipo, origem, artefato e responsável permanecem rastreáveis. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-escolha-de-origem-entre-imagem-diretorio-e-arquivo]] — Complementa o tópico com syft: escolha de origem entre imagem, diretório e arquivo.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
