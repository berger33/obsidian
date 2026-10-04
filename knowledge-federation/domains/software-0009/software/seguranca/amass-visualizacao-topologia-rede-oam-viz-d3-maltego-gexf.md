---
id: software.seguranca.tranche08.000769
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/owasp-amass/amass/master/README.md", "https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md", "https://pkg.go.dev/github.com/owasp-amass/amass/v4"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP Amass (`oam_viz` / `amass viz`): Exportação do Grafo de Superfície de Ataque para **D3.js HTML Interativo (`-d3`)**, **Gephi (`-gexf`)**, **Graphviz (`-dot`)** e **Maltego**

## Em uma frase
Ler 5.000 linhas de texto para entender quais subdomínios da empresa estão concentrados em um provedor de hospedagem legado de terceiros ou compartilhando um único certificado TLS wildcard é difícil; mas quando visto como um **grafo visual colorido por tipo de nó**, esses agrupamentos de risco saltam aos olhos imediatamente!

## Por que importa
A ferramenta **`oam_viz`** (ou **`amass viz`**) lê o banco de dados de grafo do Amass (`-dir`) e exporta a topologia completa para cinco formatos de visualização e análise de grafos: **(1) `-d3`** (gera um arquivo HTML5 autocontido com grafo interativo **D3.js** navegável no browser!), **(2) `-dot`** (Graphviz), **(3) `-gexf`** (para análise de centralidade no **Gephi**), **(4) `-graphistry`** e **(5) `-maltego`** (CSV pronto para importação no **Maltego**)!

## Como funciona
No grafo interativo `-d3`, cada classe de entidade do Open Asset Model (Domínio, Subdomínio, CNAME, Endereço IP, Netblock CIDR, ASN, Servidor NS, MX) recebe uma cor distinta, permitindo clicar e arrastar clusters inteiros da infraestrutura.

## Exemplo
```bash
# Exportar o grafo da superficie de ataque do banco do Amass para visualizacao HTML interativa D3.js e formato Gephi (GEXF)
oam_viz -dir /cases/easm/amass_db -d exemplo.com.br -d3 -gexf -o /cases/easm/viz_output
```

## Limites e trade-offs
Incluir o grafo visual gerado por `-d3` ou Gephi (`-gexf`) no relatório executivo de um Pentest / Avaliação de Superfície Externa demonstra claramente para a diretoria como domínios esquecidos em provedores externos se conectam à infraestrutura principal.

## Como verificar
Abra o arquivo HTML gerado por `-d3` e procure por nós `IPAddress` ou `Netblock` isolados fora do ASN principal da empresa ou da CDN/WAF oficial.

## Conexões
- [[amass-monitoramento-continuo-drift-superficie-ataque-oam-track]] — Veja também: OWASP Amass (`oam_track` / `amass track`): Monitoramento Contínuo de **Drift da Superfície de Ataque** e Alertas de Novos Subdomínios e Mudanças de IP.
- [[amass-engine-scripting-ads-extensibilidade-pipeline-httpx-nuclei]] — Veja também: OWASP Amass: Integração em Pipelines de Reconhecimento (**Amass -> `oam_subs` -> `httpx` -> `katana` -> `nuclei`**) e Execução Contêinerizada Docker.
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Referência cruzada direta com amass-arquitetura-easm-owasp-open-asset-model-oam-grafo.
- [[amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db]] — Referência cruzada direta com amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
