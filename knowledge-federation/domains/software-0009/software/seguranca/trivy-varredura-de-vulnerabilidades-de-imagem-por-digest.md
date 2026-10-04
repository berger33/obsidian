---
id: software.seguranca.tranche17.001601
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

# Trivy: Varredura de vulnerabilidades de imagem por digest

## Em uma frase
**Trivy — Varredura de vulnerabilidades de imagem por digest:** O modo de imagem inspeciona pacotes do sistema operacional e dependências de linguagens presentes no alvo, permitindo comparar achados entre releases imutáveis.

## Por que importa
O recorte de **varredura de vulnerabilidades de imagem por digest** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **varredura de vulnerabilidades de imagem por digest**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em CI autorizado, execute a análise de vulnerabilidades sobre `registry.example/app@sha256:...` e guarde o digest com o relatório. Teste em staging autorizado.

## Limites e trade-offs
Compare o digest e a base de vulnerabilidades usados antes de atribuir a correção a uma release. Exceções exigem responsável e prazo.

## Como verificar
Reproduza o scan do mesmo digest e confirme que pacote, advisory e severidade aparecem no formato esperado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-escolha-explicita-de-scanners]] — Complementa o tópico com trivy: escolha explícita de scanners.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
