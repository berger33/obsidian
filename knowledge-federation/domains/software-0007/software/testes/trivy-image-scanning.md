---
id: software.testes.tranche18.001239
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
fontes: ["https://trivy.dev/latest/docs/scanner/vulnerability/", "https://trivy.dev/latest/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: analisar imagens de contêiner

## Em uma frase
A imagem é analisada camada a camada, cruzando os pacotes instalados com bases de vulnerabilidades e filtrando por gravidade.

## Por que importa
A imagem é o artefato efetivamente implantado, e a análise dela detecta problemas que a árvore de dependências do código não revela.

## Como funciona
Analise a imagem após a construção e antes da publicação, filtre por gravidade relevante e opcionalmente oculte falhas ainda sem correção disponível.

## Exemplo
A verificação pode bloquear a publicação ao encontrar vulnerabilidade de gravidade alta com correção disponível.

## Limites e trade-offs
Bases de vulnerabilidades mudam diariamente, e o mesmo artefato passa a acusar falhas novas sem qualquer alteração de código, o que exige contexto na leitura.

## Como verificar
Reanalise a mesma imagem em dois momentos e compare os achados para distinguir mudança de base de mudança de artefato.

## Conexões
- [[trivy-targets-and-scanners]] — Veja também: Trivy: separar alvos e verificadores.
- [[trivy-filesystem-and-repo]] — Veja também: Trivy: analisar sistema de arquivos e repositório.

## Fontes
- [Trivy — Vulnerability scanning](https://trivy.dev/latest/docs/scanner/vulnerability/) — análise de imagens e sistemas de arquivos por vulnerabilidades; consultado em 2026-10-03.
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
