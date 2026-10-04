---
id: software.seguranca.tranche17.001604
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

# Trivy: Segredos na configuração da imagem

## Em uma frase
**Trivy — Segredos na configuração da imagem:** Metadados de imagem podem conter variáveis de ambiente ou outros valores sensíveis e têm opções de scanner próprias.

## Por que importa
O recorte de **segredos na configuração da imagem** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **segredos na configuração da imagem**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Construa uma imagem descartável com um valor-canário não secreto no `ENV` e habilite o scanner de configuração de imagem para validar a detecção. Teste em staging autorizado.

## Limites e trade-offs
Imagem não é o único local de vazamento; logs de build, argumentos, camadas antigas e repositórios precisam de controles separados. Exceções exigem responsável e prazo.

## Como verificar
Inspecione o relatório sem imprimir valores sensíveis e verifique se o canário é reconhecido no campo de origem correto. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-analise-do-sistema-de-arquivos-do-repositorio]] — Complementa o tópico com trivy: análise do sistema de arquivos do repositório.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
