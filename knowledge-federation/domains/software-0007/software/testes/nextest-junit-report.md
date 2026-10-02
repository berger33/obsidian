---
id: software.testes.tranche15.000946
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/machine-readable/junit/", "https://nexte.st/docs/configuration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: publicar resultado em JUnit XML

## Em uma frase
O nextest pode gravar relatório JUnit XML por perfil, com opções para incluir ou omitir saída de testes aprovados e para classificar resultados instáveis.

## Por que importa
A maioria das plataformas de integração consome JUnit, e um relatório bem configurado dá visibilidade por caso sem exigir leitura de log bruto.

## Como funciona
Configure a seção de relatório no perfil de integração, defina o caminho do arquivo e escolha o que armazenar para manter o tamanho razoável.

## Exemplo
Um perfil pode declarar caminho do XML, armazenamento apenas de saída de falhas e status específico para casos instáveis.

## Limites e trade-offs
Relatório com saída de todos os testes cresce rápido e pode carregar dados sensíveis, enquanto classificar instável como sucesso esconde informação relevante.

## Como verificar
Gere o relatório, abra o XML e confirme a presença de um caso falho e um instável com os status definidos na configuração.

## Conexões
- [[nextest-partitioning]] — Veja também: nextest: dividir a suíte em shards de CI.
- [[nextest-archives]] — Veja também: nextest: reutilizar binários com archive.

## Fontes
- [nextest — JUnit support](https://nexte.st/docs/machine-readable/junit/) — geração de JUnit XML e opções de relatório para integração; consultado em 2026-10-02.
- [nextest — Configuration](https://nexte.st/docs/configuration/) — perfis, overrides, retries, timeouts e grupos de teste; consultado em 2026-10-02.
