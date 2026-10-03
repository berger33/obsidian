---
id: software.testes.tranche18.001242
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://trivy.dev/latest/docs/scanner/secret/", "https://trivy.dev/latest/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: encontrar segredos expostos

## Em uma frase
O verificador de segredos procura credenciais, chaves e tokens em arquivos e camadas, com regras próprias e possibilidade de exceções.

## Por que importa
Segredos no código ou em camadas de imagem permanecem no histórico e exigem rotação, não apenas remoção do arquivo atual.

## Como funciona
Ative o verificador na análise do diretório e da imagem, trate cada achado como incidente e faça a rotação da credencial.

## Exemplo
Um token encontrado em arquivo de exemplo precisa ser revogado e substituído por variável de ambiente, além de removido do histórico.

## Limites e trade-offs
A ferramenta reduz mas não elimina falsos positivos, e segredos injetados em tempo de execução podem não aparecer na análise estática.

## Como verificar
Introduza uma credencial fictícia em arquivo de teste e confirme que ela aparece no relatório com o caminho correspondente.

## Conexões
- [[trivy-misconfiguration]] — Veja também: Trivy: detectar falhas de configuração.
- [[trivy-sbom]] — Veja também: Trivy: gerar e consumir inventário de software.

## Fontes
- [Trivy — Secret scanning](https://trivy.dev/latest/docs/scanner/secret/) — procura de credenciais e chaves em arquivos e camadas; consultado em 2026-10-03.
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
