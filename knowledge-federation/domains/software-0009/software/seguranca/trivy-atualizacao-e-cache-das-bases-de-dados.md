---
id: software.seguranca.tranche17.001609
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

# Trivy: Atualização e cache das bases de dados

## Em uma frase
**Trivy — Atualização e cache das bases de dados:** Os resultados dependem de bases e bundles auxiliares que o scanner consulta ou mantém em cache; a execução offline precisa declarar sua origem.

## Por que importa
O recorte de **atualização e cache das bases de dados** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **atualização e cache das bases de dados**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Faça duas execuções controladas com cache conhecido e registre horário da atualização de banco junto com a evidência do pipeline. Teste em staging autorizado.

## Limites e trade-offs
Cache antigo pode ocultar advisories recentes; acesso à rede, mirror e versão da base alteram o resultado. Exceções exigem responsável e prazo.

## Como verificar
Inspecione logs de atualização, política de mirror e carimbo de data da base; simule cache indisponível para observar o comportamento. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-priorizacao-de-remediacao-pela-classe-do-achado]] — Complementa o tópico com trivy: priorização de remediação pela classe do achado.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
