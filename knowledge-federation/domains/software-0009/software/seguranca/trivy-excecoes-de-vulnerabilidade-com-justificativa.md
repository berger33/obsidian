---
id: software.seguranca.tranche17.001608
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

# Trivy: Exceções de vulnerabilidade com justificativa

## Em uma frase
**Trivy — Exceções de vulnerabilidade com justificativa:** Exceções podem reduzir ruído, mas devem ser identificáveis por advisory e escopo, com revisão e prazo definidos pela política da equipe.

## Por que importa
O recorte de **exceções de vulnerabilidade com justificativa** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exceções de vulnerabilidade com justificativa**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use uma fixture com advisory conhecido e documente exceção limitada ao identificador e ao artefato afetado. Teste em staging autorizado.

## Limites e trade-offs
Uma exceção ampla ou sem validade transforma um achado temporário em risco invisível, inclusive após mudança do componente. Exceções exigem responsável e prazo.

## Como verificar
Confirme que a exceção afeta somente o finding autorizado e que o relatório mantém trilha da decisão e do prazo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-atualizacao-e-cache-das-bases-de-dados]] — Complementa o tópico com trivy: atualização e cache das bases de dados.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
