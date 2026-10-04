---
id: software.seguranca.tranche06.000527
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/google/timesketch/master/README.md", "https://timesketch.org/guides/user/sketch-overview/", "https://timesketch.org/guides/admin/install/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Timesketch: Aba **Intelligence**, Marcação de IOCs na Timeline e Integração com Plataformas de CTI (Yeti, MISP e OpenCTI)

## Em uma frase
A aba **Intelligence** de um Sketch no Timesketch funciona como um repositório centralizado de Indicadores de Comprometimento (IPs, domínios, hashes SHA-256, caminhos de arquivos, mutexes, contas comprometidas) descobertos durante a análise da timeline ou importados de plataformas externas de CTI.

## Por que importa
Quando um analista descobre um endereço IP de C2 em um log de firewall na Timeline 1 e o adiciona à aba *Intelligence* do Sketch, ele pode clicar no ícone de lupa ao lado do indicador para buscar instantaneamente aquele mesmo IOC em todas as outras 20 timelines do Sketch e rotular todos os eventos correspondentes com a tag `ioc`.

## Como funciona
Além da adição manual direto da linha do evento, o analyzer de inteligência conecta-se a plataformas como **Yeti**, **MISP** e **OpenCTI** para cruzar automaticamente todos os hashes, domínios e IPs extraídos das timelines do Sketch contra o grafo corporativo de Threat Intelligence.

## Exemplo
```python
# Adicionar um indicador descoberto na investigacao diretamente aos atributos de Intelligence do Sketch via API
sketch.add_attribute(
    name="intelligence",
    values=[{
        "ioc": "198.51.100.214",
        "type": "ipv4",
        "externalURI": "https://opencti.soc.internal.corp/dashboard/observations/indicators",
        "tags": ["c2-cobaltstrike", "confirmed-exfil"]
    }],
    ontology="intelligence"
)
```

## Limites e trade-offs
Sempre preencha as `tags` semânticas ao adicionar um IOC na aba *Intelligence* do Sketch (ex.: `ransomware-dropper`, `lateral-movement-source`), pois essas tags são propagadas para os eventos da timeline facilitando a filtragem por fase do ataque.

## Como verificar
Adicione um IOC na aba *Intelligence* e acione a busca cruzada para confirmar a marcação automática dos eventos correspondentes nas timelines.

## Conexões
- [[timesketch-investigacao-guiada-dfiq-questions-facets-approaches]] — Veja também: Timesketch: Investigação Guiada com **DFIQ** (*Digital Forensics Investigative Questions* — Scenarios, Facets, Questions e Approaches).
- [[timesketch-narrativa-forense-stories-grafos-relatorios-markdown]] — Veja também: Timesketch: Construção de Relatórios Forenses Reprodutíveis com **Stories**, Agregações Gráficas e Grafos de Relacionamento.
- [[timesketch-analisadores-automaticos-analyzers-chain-tagger-similarity]] — Referência cruzada direta com timesketch-analisadores-automaticos-analyzers-chain-tagger-similarity.
- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — Referência cruzada direta com opencti-arquitetura-stix21-knowledge-graph-graphql-filigran.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.
