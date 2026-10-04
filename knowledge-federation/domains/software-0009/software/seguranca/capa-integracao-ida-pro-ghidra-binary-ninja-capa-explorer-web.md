---
id: software.seguranca.tranche13.001227
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/capa/master/README.md", "https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Integração do `capa` com **Ghidra, IDA Pro, Binary Ninja** e **`capa Explorer Web`**: Navegação Interativa e Renomeação de Funções na Engenharia Reversa

## Em uma frase
Durante a engenharia reversa de um binário no **Ghidra**, no **IDA Pro** ou no **Binary Ninja**, alternar constantemente entre a janela do terminal (onde rodou o `capa -vv`) e o desmontador copiando e colando endereços hexadecimais atrasa o trabalho do analista. Como integrar os resultados do `capa` diretamente dentro da interface gráfica do seu desmontador favorito ou explorá-los no navegador?

## Por que importa
O ecossistema oficial do `capa` oferece duas ferramentas visuais de altíssima produtividade: **(1) Os plugins nativos para IDA Pro (`capa explorer`), Ghidra e Binary Ninja**, que rodam o `capa` (ou importam o JSON gerado por `capa -j`), exibem uma árvore interativa de capacidades onde clicar em qualquer item salta instantaneamente a janela de disassembly/decompiler para a instrução exata e permite **adicionar bookmarks, colorir instruções e renomear funções (`sub_401520` -> `inject_remote_thread`)**; e **(2) O `capa Explorer Web` (`https://mandiant.github.io/capa/explorer/`)**!

## Como funciona
O **`capa Explorer Web`** é uma Single-Page Application (SPA) oficial (que também vem embutida nos pacotes standalone do `capa` para uso 100% offline em redes isoladas de laboratório!) onde você carrega o arquivo `relatorio_capa.json` (`capa -j`) para filtrar, buscar, expandir árvores de regras estáticas ou dinâmicas e compartilhar a visualização com toda a equipe!

## Exemplo
```bash
# Gerar o relatorio JSON completo do capa (estatico ou dinamico) pronto para abrir no capa Explorer Web ou importar no Ghidra/IDA
capa -j ./amostras/backdoor_implant.exe > ./backdoor_implant_capa.json
```

## Limites e trade-offs
Em laboratórios de análise de malware isolados da internet (*air-gapped*), nunca envie amostras ou relatórios de incidentes sensíveis para aplicações externas: utilize a versão **offline local do `capa Explorer Web`** incluída nos pacotes de release oficiais do `mandiant/capa`!

## Como verificar
No Ghidra, a integração do `capa` utiliza os scripts oficiais em Python/PyGhidra do repositório `capa/capa/ghidra/` para anotar diretamente os comentários de pré/pós-instrução no Decompiler.

## Conexões
- [[capa-analise-dinamica-relatorios-sandbox-cape-drakvuf-vmray-processos]] — Veja também: Análise Dinâmica com o `capa`: Extraindo Capacidades de Relatórios de **Sandboxes (`CAPE`, `DRAKVUF`, `VMRay`)** e Filtrando por **PID (`--restrict-to-processes`)**.
- [[capa-mapeamento-mitre-attack-malware-behavior-catalog-mbc-diferencas]] — Veja também: Por que o `capa` Mapeia Simultaneamente para o **MITRE ATT&CK** e para o **Malware Behavior Catalog (`MBC`)**? Entendendo a Diferença Técnica.
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Referência cruzada direta com capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant.
- [[capa-modos-saida-verbose-vv-enderecos-funcoes-json-automacao]] — Referência cruzada direta com capa-modos-saida-verbose-vv-enderecos-funcoes-json-automacao.
- [[floss-integracao-ida-pro-ghidra-binary-ninja-relatorio-html]] — Referência cruzada direta com floss-integracao-ida-pro-ghidra-binary-ninja-relatorio-html.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
